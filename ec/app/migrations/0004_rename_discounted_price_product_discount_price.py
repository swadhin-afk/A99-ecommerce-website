# Generated by Django 5.1.4 on 2024-12-30 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_discount_price_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discounted_price',
            new_name='discount_price',
        ),
    ]