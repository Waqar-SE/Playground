from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from core.models import model_choices


class AppUser(AbstractUser):
    username = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


class Meal(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField("Ingredient")

    @property
    def is_halal(self):
        # Compute it from the ingredients
        return True

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("core:meal-update", args=[self.id])


class Ingredient(models.Model):
    name = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=20)
    e_number = models.ForeignKey("ENumber", on_delete=models.PROTECT)
    is_halal = models.CharField(
        max_length=1,
        choices=model_choices.IngredientChoices.choices,
        default=model_choices.IngredientChoices.N,
    )

    def __str__(self) -> str:
        return self.name


class ENumber(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.number
