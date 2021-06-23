from django import forms
from recipes.recipe.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Recipe Title',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': '"detail-img"',
                    'placeholder': 'Enter Picture URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'recipe-info',
                    'placeholder': 'Enter Recipe Description',
                    'rows': 3,
                    'style': 'resize:none;',
                }
            ),
            'ingredients': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Recipe Ingredients, separated by comma ","',
                }
            ),
            'time': forms.NumberInput(
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Enter prepare time',
                }
            )
        }
