# Generated by Django 3.2.9 on 2021-11-10 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
