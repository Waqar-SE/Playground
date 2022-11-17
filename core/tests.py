from django.test import TestCase
from django.urls import reverse
from core import models

# Create your tests here.


class MealTestCase(TestCase):
    def test_meal_list(self):
        response = self.client.get(reverse("core:meal-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [])

    def test_meal_post(self):
        models.Ingredient.objects.create(
            name="chicken",
            origin="Poltury",
            e_number=models.ENumber.objects.create(number="E300"),
        )

        response = self.client.post(
            reverse("core:meal-create"),
            data={"name": "New one", "ingredients": [1]},
            follow=False,
        )
        self.assertTrue(models.Meal.objects.all().exists())
        self.assertEqual(response.status_code, 302)
