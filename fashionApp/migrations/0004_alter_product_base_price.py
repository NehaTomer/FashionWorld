# Generated by Django 4.2 on 2023-05-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionApp', '0003_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='base_price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
