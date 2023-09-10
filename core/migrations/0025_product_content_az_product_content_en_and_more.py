# Generated by Django 4.2.4 on 2023-09-09 13:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_discount_product_shipping_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_es',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_es',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
