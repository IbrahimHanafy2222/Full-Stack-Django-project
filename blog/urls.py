from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('About/', views.about, name='About'),
    path('Contact/', views.contact, name='Contact'),
    path('men/', views.men, name='men'),
    path('product/', views.product, name='product'),
        ]
