from . import views
from django.urls import path

app_name = "products"

urlpatterns = [
    path("", views.ProductList.as_view(), name="products"),
    path("category/", views.CategoryList.as_view(), name="category"),
    path("subcategory/", views.SubCategoryList.as_view(), name="subcategory"),
]