from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.


# class AboutPage(TemplateView):
#     template_name = 'about.html'

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')

def base(request):
    return render(request, 'base.html')


























