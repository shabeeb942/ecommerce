from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Categorie)
class CategoriesAdmin(admin.ModelAdmin):
        list_display = ('category',)
        search_fields = ('category',)
@admin.register(SubCategorie)
class SubCategoriesAdmin(admin.ModelAdmin):
        list_display = ('sub_category',)
        search_fields = ('sub_category',)
        autocomplete_fields = ('category',)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ("name",)
        search_fields = ('sub_category',)
        autocomplete_fields = ('sub_category',)


