from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=120)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category']

    def __str__(self):
        return self.category


class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=120)


    class Meta:
        verbose_name = 'subcategories'
        verbose_name_plural = 'subcategories'
        ordering = ['sub_category']

    def __str__(self):
        return self.sub_category


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    name  = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products/")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
