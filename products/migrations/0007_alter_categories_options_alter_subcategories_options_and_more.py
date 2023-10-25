# Generated by Django 4.2.4 on 2023-10-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_categorie_categories_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['category'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategories',
            options={'ordering': ['sub_category'], 'verbose_name': 'subcategories', 'verbose_name_plural': 'subcategories'},
        ),
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(default=1, upload_to='categories/'),
            preserve_default=False,
        ),
    ]
