from django.contrib import admin
from recipes.recipe.models import Recipe


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_url', 'description', 'ingredients', 'time']
    list_filter = []
    sorted_by = []
