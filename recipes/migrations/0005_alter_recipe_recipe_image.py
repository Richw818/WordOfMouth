# Generated by Django 4.0.2 on 2022-03-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
