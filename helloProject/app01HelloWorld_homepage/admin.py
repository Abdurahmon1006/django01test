from django.contrib import admin
from .forms import *
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    froms = BookForm

class TalabaAdmin(admin.ModelAdmin):
    froms = TalabaForm

class XizmatAdmin(admin.ModelAdmin):
    froms = XizmatForm

admin.site.register(Book, BookAdmin)
admin.site.register(Talaba)
admin.site.register(Xizmat)
# admin.site.register()
# admin.site.register()
# admin.site.register()