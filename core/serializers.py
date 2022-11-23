from rest_framework import serializers
from core import models


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = [
            "name",
            "origin",
            "e_number",
            "is_halal",
        ]


class ENumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ENumber
        fields = ["number"]
