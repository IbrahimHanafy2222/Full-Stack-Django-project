from django.shortcuts import render
from .models import *
# Create your views here.
def about(request):
    return render(request,'blog/About.html')

def blog(request):
    Products=Product.objects.all()
    Best=Best_Selling.objects.all()
    New_Arrivals=New_Arrival.objects.all()
    pants=Pants.objects.all()
    winters=Winter.objects.all()
    return render(request, 'blog/index.html',{'Products':Products,'Best':Best,'New_Arrivals':New_Arrivals ,'pants':pants,'winters':winters})

def contact(request):
    return render(request,'blog/Contact.html')

def men(request):
    men=Men.objects.all()
    return render(request,'blog/men.html',{'men':men})

def product(request):
    men=Men.objects.all()
    return render(request,'blog/Product.html',{'men':men})