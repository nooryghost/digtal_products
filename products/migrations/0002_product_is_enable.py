# Generated by Django 3.2 on 2023-02-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='is_enable'),
        ),
    ]
