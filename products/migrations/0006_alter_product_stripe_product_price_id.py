# Generated by Django 4.2.1 on 2023-07-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_stripe_product_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
