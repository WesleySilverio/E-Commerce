from django.shortcuts import render
from django.views import View
from .models import Product


# Create your views here.

def home(request):
    return render(request,"home.html")

class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category = val)
        return render(request, "category.html", locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        details = Product.objects.get(pk = pk)
        return render(request, "productdetail.html", locals())