from django.db import models


class IngredientChoices(models.TextChoices):
    H = ("H", "Halal")
    N = ("N", "Not Halal")
    C = ("C", "Conditional")
