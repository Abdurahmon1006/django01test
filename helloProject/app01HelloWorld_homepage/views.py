from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def homePageviev(request):
    return HttpResponse("<h1>   Salom dunyo!</h1>"
                        "<p1> =)        </p1>"
                        )

    href = "http://127.0.0.1:8000/base/"
    href = "base"

def homePageviev2(request):
    return HttpResponse("Salom"
                        "<p1> *_*  =) !!!!!! ^_^ </p1>")


    href = "http://127.0.0.1:8000/base/"
    href = "base"


