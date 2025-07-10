from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from config import settings
from sodda_sahifalar_app.models import Xizmat, Maxsulot


# Create your views here.


# class AboutPage(TemplateView):
#     template_name = 'about.html'

def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        full_message = f"{email} dan sizga quyidagi xabar keldi:\n\n\n{message}"

        try:
            send_mail(
                f'{name} sizga xabar yubordi.',
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER, ],
                fail_silently=False,
            )
            return redirect('index')
        except Exception as e:
            print(f"Email yuborishda xato: {e}")
            return HttpResponse(f"xato yuz berdi: {e}")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        full_message = f"{email} dan sizga quyidagi xabar keldi:\n\n\n{message}"

        try:
            send_mail(
                f'{name} sizga xabar yubordi.',
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER, ],
                fail_silently=False,
            )
            return redirect('contact')
        except Exception as e:
            print(f"Email yuborishda xato: {e}")
            return HttpResponse(f"xato yuz berdi: {e}")
    maxsulotlar = Maxsulot.objects.all()
    return render(request, 'contact.html', {'maxsulotlar': maxsulotlar})


def services(request):
    xizmatlar = Xizmat.objects.all()
    return render(request, 'services.html', {'xizmatlar': xizmatlar})



def testimonials(request):
    return render(request, 'testimonials.html')

def base(request):
    return render(request, 'base.html')

def extra(request):
    return render(request, 'extra.html')


























