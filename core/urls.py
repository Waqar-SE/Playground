from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import views, api

app_name = "core"

api_patterns = [
    path(
        "ingredients/",
        api.IngredientViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="ingredients",
    )
]

router = DefaultRouter()
router.register(r"enumbers", api.ENumberViewSet, basename="e-numbers")

urlpatterns = [
    path("meals/", views.ListMealView.as_view(), name="meal-list"),
    path("meals/create/", views.CreateMealView.as_view(), name="meal-create"),
    path("meals/<int:pk>/update/", views.DetailMealView.as_view(), name="meal-update"),
    path("meals/<int:pk>/delete/", views.DeleteMealView.as_view(), name="meal-delete"),
    path("api/", include(api_patterns)),
    path("router/", include(router.urls)),
]
