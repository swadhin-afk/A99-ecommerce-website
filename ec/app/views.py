from django.db.models import Count
from django.shortcuts import render 
from django.views import View
from. models import Product
# Create your views here.

def home (request):
    return render (request,"app/home.html")
class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category='value') 
        title = Product.objects.filter(category='value').value('product').annotate(total=Count('product'))
        return render(request,"app/category.html",locals())
