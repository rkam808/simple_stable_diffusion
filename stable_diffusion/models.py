from django.db import models

class Prompt(models.Model):
    description = models.CharField(default='', max_length=1000)
    type = models.CharField(default='', max_length=100)
    
    def __str__(self):
        return self.description

class Example(models.Model):
    name = models.CharField(default='', max_length=100)
    image_path = models.CharField(default='', max_length=100)
    prompts = models.ManyToManyField(Prompt)
    style_prompt = models.CharField(default='', max_length=1000)
    character_prompt = models.CharField(default='', max_length=1000)
    negative_prompt = models.CharField(default='', max_length=1000)
    
    def __str__(self):
        return self.name