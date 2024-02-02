from django.shortcuts import render
from django.views.generic import DetailView
from car.models import Car
from brand.models import Brand

def home(request, brand_slug = None):
    cars = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug= brand_slug)
        cars = Car.objects.filter(brand= brand)
    brands = Brand.objects.all()
    return render(request,'home.html',{'category': brands, 'cars': cars})