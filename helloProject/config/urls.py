import os
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01HelloWorld_homepage.urls')),
    path('', include('app01HelloWorld_homepage.urls')),
    path('', include('sodda_sahifalar_app.urls')),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'static'))