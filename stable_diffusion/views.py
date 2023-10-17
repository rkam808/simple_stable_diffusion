from django.shortcuts import render
from stable_diffusion.models import Example
import requests

def home(request):
    examples = Example.objects.all()
    return render(request, 'stable_diffusion/home.html', context={'examples': examples})

def generate(request):
    endpoint = 'https://stablediffusionapi.com/api/v3/text2img'
    style = request.GET.get('style')
    subject = request.GET.get('subject')
    negative_prompt = request.GET.get('negative_prompt') + 'NSFW'
    prompt = style + '. ' + subject
    key = request.GET.get('key')
    data = {
        'key': key,
        'prompt': prompt,
        'negative_prompt': negative_prompt,
        'width': '512',
        'height': '512',
        'samples': '1'
    }
    response = requests.post(endpoint, data=data)
    data = response.json()
    
    if data['status'] == 'success':
        image_url = data['output'][0]
        return render(request, 'stable_diffusion/generated_image.html', context={'image_url':image_url})
    else:
        return render(request, 'stable_diffusion/home.html', context={'error':''})
