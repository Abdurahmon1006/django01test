from django.urls import path
from sodda_sahifalar_app.views import about, index, contact, services, testimonials

urlpatterns = [
path('about/', about, name='about' ),
path('', about, name='about' ),
path('index/', index, name='index' ),
path('contact/', contact, name='contact' ),
path('services/', services, name='services' ),
path('testimonials/', testimonials, name='testimonials' ),
path('base/', testimonials, name='base' ),



]

