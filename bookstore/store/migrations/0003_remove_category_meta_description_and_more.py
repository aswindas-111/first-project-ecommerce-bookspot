# Generated by Django 4.2.4 on 2023-08-17 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_author_product_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_title',
        ),
    ]
