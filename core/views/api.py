from rest_framework.viewsets import ModelViewSet
from core import serializers, models


class IngredientViewSet(ModelViewSet):
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        return models.Ingredient.objects.all()


class ENumberViewSet(ModelViewSet):
    serializer_class = serializers.ENumberSerializer

    def get_queryset(self):
        return models.ENumber.objects.all()
