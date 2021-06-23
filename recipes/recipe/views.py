from django.shortcuts import render, redirect
from recipes.recipe.forms import RecipeForm
from recipes.recipe.models import Recipe


# Create your views here.


def get_id(pk):
    return Recipe.objects.get(pk=pk)


def show_form(req, form, temp):
    context = {
        'form': form
    }
    return render(req, temp, context)


def save_form(req, form, temp):
    if form.is_valid():
        form.save()
        return redirect('index')
    return show_form(req, form, temp)


def index(req):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(req, 'index.html', context)


def create_recipe(req):
    if req.method == 'GET':
        form = RecipeForm()
        return show_form(req, form, 'create.html')
    form = RecipeForm(req.POST)
    return save_form(req, form, 'index.html')


def edit_recipe(req, pk):
    recipe = get_id(pk)
    if req.method == 'GET':
        form = RecipeForm(initial=recipe.__dict__)
        return show_form(req, form, 'edit.html')
    form = RecipeForm(
        req.POST,
        instance=recipe,
    )
    return save_form(req, form, 'edit.html')


def delete_recipe(req, pk):
    recipe = get_id(pk)
    if req.method == 'GET':
        form = RecipeForm(initial=recipe.__dict__, )
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        form.save(commit=False)
        return show_form(req, form, 'delete.html')
    recipe.delete()
    return redirect('index')


def details(req, pk):
    recipe = get_id(pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(req, 'details.html', context)
