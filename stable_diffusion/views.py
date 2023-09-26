from django.shortcuts import render
import requests

def home(request):
    return render(request, 'stable_diffusion/home.html')

def generate(request):
    return render(request, 'stable_diffusion/generated_image.html')
