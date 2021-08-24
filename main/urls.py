from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('create', views.create, name='create'),
    path('photo', views.photo, name='photo'),
    path('upload/', views.photo),
]
