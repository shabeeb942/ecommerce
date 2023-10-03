from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,Categories,SubCategories
# Create your views here.

class CategoryList(ListView):
    model = Categories
    template_name = "products/category.html"


class SubCategoryList(ListView):
    model = SubCategories
    template_name = "products/subcategory.html"


class ProductList(ListView):
    model = Product
    template_name = "products/products.html"
