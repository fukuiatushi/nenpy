from django.contrib import admin
from django.urls import path, include
from .import views

app_name = "fuel"


urlpatterns = [
    path("", views.record_list, name="record_list"),
    path("add/", views.record_add, name="record_add"),
    path("<int:pk>/", views.record_detail, name="record_detail"),
    path("<int:pk>/edit/", views.record_edit, name="record_edit")
]
