# Generated by Django 4.0.6 on 2022-08-17 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_product_image_pictuers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictuers',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name=' المنتج'),
        ),
    ]
