from django.contrib import admin
from .forms import *
from .models import *

# Register your models here.

class MaxsulotAdmin(admin.ModelAdmin):
    froms = MaxsulotForm


class XizmatAdmin(admin.ModelAdmin):
    froms = XizmatForm

admin.site.register(Maxsulot)
admin.site.register(Xizmat)
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()