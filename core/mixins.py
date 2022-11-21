from core import models
from django.urls import reverse_lazy


class MealMixin:
    success_url = reverse_lazy("core:meal-list")

    def get_queryset(self):
        return models.Meal.objects.all()
