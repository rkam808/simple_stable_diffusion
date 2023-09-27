from django.shortcuts import render
import requests

def home(request):
    return render(request, 'stable_diffusion/home.html')

def generate(request):
    endpoint = 'https://stablediffusionapi.com/api/v3/text2img'
    prompt = request.GET.get('prompt')
    data = {
        'key': 'dummy_key',
        'prompt': prompt,
        'width': '512',
        'height': '512',
        'samples': '1'
    }
    response = requests.post(endpoint, data=data)
    data = response.json()

    {
        "status":"success",
        "generationTime":4.142760515213013,
        "id":45126007,
        "output":["https:\\/\\/cdn2.stablediffusionapi.com\\/generations\\/5eed2d8e-b00b-4649-961a-fbe3081ed227-0.png"],
        "meta":{
            "H":512,
            "W":512,
            "enable_attention_slicing":"true"
            ,"file_prefix":"5eed2d8e-b00b-4649-961a-fbe3081ed227"
            ,"guidance_scale":7,
            "instant_response":"no",
            "model":"runwayml\\/stable-diffusion-v1-5",
            "n_samples":1,
            "negative_prompt":"low quality",
            "outdir":"out",
            "prompt":"anime girl blue hair",
            "revision":"fp16",
            "safetychecker":"no",
            "seed":2101081969,
            "steps":20,
            "vae":"stabilityai\\/sd-vae-ft-mse"
        }
    }
    
    if data['status'] == 'success':
        image_url = data['output'][0]
        return render(request, 'stable_diffusion/generated_image.html', context={'image_url':image_url})
    else:
        return render(request, 'stable_diffusion/home.html')
