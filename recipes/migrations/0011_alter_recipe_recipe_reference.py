# Generated by Django 4.0.2 on 2022-04-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipe_recipe_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_reference',
            field=models.IntegerField(),
        ),
    ]
