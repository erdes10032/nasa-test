from django.shortcuts import render
from .models import SliderImage


def index(request):
    slides = SliderImage.objects.all()
    return render(request, 'index.html', {
        'slides': slides
    })