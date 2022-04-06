from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Recipe
from .forms import RecipeForm
import boto3

class homeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/homepage.html'
    context_object_name = 'recipelist'

def index(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        # file = request.FILES.get('recipe_image', False)
        # filename = 'x'
        # s3 = boto3.resource('s3', aws_access_key_id='AKIA6PI7GGPQBJIKMAVI', aws_secret_access_key='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')
        # bucket = s3.Bucket('wordofmouth-images')
        # bucket.put_object(Key=filename, Body=file)
        if recipe_form.is_valid():
            recipe_form.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipes/recipeLayout.html', {
            'recipe_form': recipe_form})

def detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    is_favorited = False
    if recipe.favorites.filter(id=request.user.id).exists():
        is_favorited = True
    context = {
        'recipe': recipe,
        'is_favorited': is_favorited
    }
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/detail.html', context)

def result(request):
    return render(request, 'recipes/success.html')

def short(request):
    recipelist = [r for r in Recipe.objects.all() if r.is_short()]
    context = {'recipelist': recipelist}
    return render(request, 'recipes/shortRecipes.html', context)

def long(request):
    recipelist = [r for r in Recipe.objects.all() if not r.is_short()]
    context = {'recipelist': recipelist}
    return render(request, 'recipes/longRecipes.html', context)

def fork(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.save()
            # new_recipe = recipe_form.save(commit=False)
            # new_recipe.recipe_image = recipe.recipe_image
            # new_recipe.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipes/forkRecipe.html', {'recipe': recipe})

def add(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
        text = request.POST['instruction']
        recipe.recipeinstruction_set.create(instruction_text = text)
        recipe.num_instructions += 1
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def myrecipes(request):
    return render(request, 'recipes/myRecipes.html')

def favorited_list(request):
    user = request.user
    favorite_recipes = user.favorites.all()
    context = {'favorite_recipes': favorite_recipes}
    return render(request, 'recipes/favoritedRecipes.html',context)

def favorite_recipe(request):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    is_favorited = False
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        is_favorited = False
    else:
        recipe.favorites.add(request.user)
        is_favorited = True
    return HttpResponseRedirect(recipe.get_absolute_url())