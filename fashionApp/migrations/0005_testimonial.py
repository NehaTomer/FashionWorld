# Generated by Django 4.2 on 2023-05-31 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionApp', '0004_alter_product_base_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='testimonial')),
                ('name', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
