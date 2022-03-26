from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 50, default = '')
    recipe_ingredients = models.CharField(max_length = 500, default = '')
    recipe_equipment = models.CharField(max_length = 500, default = '')
    recipe_instructions = models.CharField(max_length = 1000, default = '')
    recipe_image = models.ImageField(default='', upload_to='media/')
    def __str__(self):
        return self.recipe_name

    def is_short(self):
        length = len(self.recipe_instructions)
        return length <= 500
    
    