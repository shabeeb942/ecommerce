from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,Categorie,SubCategorie
# Create your views here.

class CategoryList(ListView):
    model = Categorie
    template_name = "products/category.html"


class SubCategoryList(ListView):
    model = SubCategorie
    template_name = "products/subcategory.html"


class ProductList(ListView):
    model = Product
    template_name = "products/products.html"

