# Generated by Django 4.0.2 on 2022-04-23 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0038_recipe_recipe_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_type',
        ),
        migrations.AddField(
            model_name='recipe',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
