# Generated by Django 4.0.6 on 2022-08-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_pictuers_product_pictuers_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='صورة العرض'),
        ),
    ]