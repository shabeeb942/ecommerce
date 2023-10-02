from django.db import models

# Create your models here.

class Categorie(models.Model):
    category = models.CharField(max_length=120)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.category


class SubCategorie(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=120)

    class Meta:
        ordering = ('sub_category',)

    def __str__(self):
        return self.sub_category


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategorie, on_delete=models.CASCADE)
    name  = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products/")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
