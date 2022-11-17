from django import forms
from core import models


class MealForm(forms.ModelForm):
    class Meta:
        model = models.Meal
        fields = ["name", "ingredients"]
