from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("meals", views.ListMealView.as_view(), name="meal-list"),
    path("meals/create", views.CreateMealView.as_view(), name="meal-create"),
    path("meals/<int:pk>/update", views.DetailMealView.as_view(), name="meal-update"),
    path("meals/<int:pk>/delete", views.DeleteMealView.as_view(), name="meal-delete"),
]
