from django.urls import path
from app01HelloWorld_homepage.views import homePageviev, homePageviev2

urlpatterns = [
    path('hpme', homePageviev, name='home'),
    path('home2/', homePageviev2, name='home2'),

]






