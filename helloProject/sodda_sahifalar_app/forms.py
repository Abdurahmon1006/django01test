from django.forms import forms
from .models import *


class MaxsulotForm(forms.Form):
    class Meta:
        model = Maxsulot
        fields = ['nomi', 'narxi', 'tavsifi', 'tasviri']



class XizmatForm(forms.Form):
    class Meta:
        model = Xizmat
        fields = ['xizmatnomi','xizmatturi', 'narxi', 'ishsoati']