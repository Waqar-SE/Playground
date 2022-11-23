from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.edit import CreateView
from core import forms, mixins


class CreateMealView(CreateView):
    template_name = "core/form_templates/meal_create_form.html"
    success_url = reverse_lazy("core:meal-list")
    form_class = forms.MealForm


class ListMealView(mixins.MealMixin, ListView):
    template_name = "core/list/meal_list.html"


class DetailMealView(mixins.MealMixin, UpdateView):
    template_name = "core/form_templates/meal_update.html"
    fields = ["name", "ingredients"]


class DeleteMealView(mixins.MealMixin, DeleteView):
    template_name = "core/form_templates/meal_delete.html"
