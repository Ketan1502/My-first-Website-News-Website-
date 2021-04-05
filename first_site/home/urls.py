from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('news',views.newssource,name='news'),
    path('contact',views.contact,name='contact'),   
]
