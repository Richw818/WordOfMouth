from django.test import TestCase

# Create your tests here.
from .models import Recipe, RecipeInstruction

class TestRecipe(TestCase):
    def test_short_recipe(self):
        r = Recipe.objects.create(recipe_name = "1", recipe_ingredients = "1", recipe_instructions = "1")
        self.assertIs(r.is_short(), True)

    def test_long_recipe(self):
        r = Recipe.objects.create(recipe_name = "1", recipe_ingredients = "1", 
        recipe_instructions = "Procedure: Preheat the oven to 325 degrees F (165 degrees C). Grease cookie sheets or line with parchment paper. Sift together the flour, baking soda and salt; set aside. In a medium bowl, cream together the melted butter, brown sugar and white sugar until well blended. Beat in the vanilla, egg, and egg yolk until light and creamy. Mix in the sifted ingredients until just blended. Stir in the chocolate chips by hand using a wooden spoon. Drop cookie dough 1/4 cup at a time onto the prepared cookie sheets. Cookies should be about 3 inches apart. Bake for 15 to 17 minutes in the preheated oven, or until the edges are lightly toasted. Cool on baking sheets for a few minutes before transferring to wire rack.")
        self.assertIs(r.is_short(), False)

    def test_add_instruction(self):
        r = Recipe.objects.create()
        r.recipeinstruction_set.create(instruction_text = 'new instruction')
        self.assertIs(r.recipeinstruction_set.count(), 1)

    def test_add_instruction2(self):
        r = Recipe.objects.create()
        r.recipeinstruction_set.create(instruction_text = 'new instruction')
        self.assertEquals(r.recipeinstruction_set.first().instruction_text, 'new instruction')

    def test_add_equipment(self):
        r = Recipe.objects.create()
        r.recipeequipment_set.create(equipment_text = 'new equipment')
        self.assertIs(r.recipeequipment_set.count(), 1)

    def test_add_equipment2(self):
        r = Recipe.objects.create()
        r.recipeequipment_set.create(equipment_text = 'new equipment')
        self.assertEquals(r.recipeequipment_set.first().equipment_text, 'new equipment')

    def test_add_ingredient(self):
        r = Recipe.objects.create()
        r.recipeingredient_set.create(ingredient_text = 'new ingredient', ingredient_quantity = '6')
        self.assertIs(r.recipeingredient_set.count(), 1)

    def test_add_ingredient2(self):
        r = Recipe.objects.create()
        r.recipeingredient_set.create(ingredient_text = 'new ingredient', ingredient_quantity = '6')
        self.assertEquals(r.recipeingredient_set.first().ingredient_text, 'new ingredient')
        self.assertEquals(r.recipeingredient_set.first().ingredient_quantity, '6')

    def test_edit_name(self):
        r = Recipe.objects.create()
        r.recipe_name = 'Name 1'
        self.assertEquals(r.recipe_name, 'Name 1')
        r.recipe_name = 'Name 2'
        self.assertEquals(r.recipe_name, 'Name 2')

    def test_edit_description(self):
        r = Recipe.objects.create()
        r.recipe_description = 'Description 1'
        self.assertEquals(r.recipe_description, 'Description 1')
        r.recipe_description = 'Description 2'
        self.assertEquals(r.recipe_description, 'Description 2')

    def test_edit_equipment(self):
        r = Recipe.objects.create()
        r.recipe_equipment = 'Equipment 1'
        self.assertEquals(r.recipe_equipment, 'Equipment 1')
        r.recipe_equipment = 'Equipment 2'
        self.assertEquals(r.recipe_equipment, 'Equipment 2')

    def test_edit_ingredient(self):
        r = Recipe.objects.create()
        r.recipe_ingredients = 'Ingredient 1'
        self.assertEquals(r.recipe_ingredients, 'Ingredient 1')
        r.recipe_ingredients = 'Ingredient 2'
        self.assertEquals(r.recipe_ingredients, 'Ingredient 2')

    def test_edit_instruction(self):
        r = Recipe.objects.create()
        r.recipe_instructions = 'Instruction 1'
        self.assertEquals(r.recipe_instructions, 'Instruction 1')
        r.recipe_instructions = 'Instruction 2'
        self.assertEquals(r.recipe_instructions, 'Instruction 2')
    