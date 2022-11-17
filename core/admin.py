from django.contrib import admin
from core import models


@admin.register(models.Meal)
class MealAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ENumber)
class ENumberAdmin(admin.ModelAdmin):
    pass
