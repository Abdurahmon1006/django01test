from django.forms import forms
from .models import *


class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = ['name', 'title', 'author']

class TalabaForm(forms.Form):
    class Meta:
        model = Talaba
        fields = ['ism', 'familya', 'yosh']

class XizmatForm(forms.Form):
    class Meta:
        model = Xizmat
        fields = ['Xizmatturi', 'narxi', 'ishsoati']