# Generated by Django 4.0.2 on 2022-04-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0029_recipe_recipe_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_time',
        ),
    ]
