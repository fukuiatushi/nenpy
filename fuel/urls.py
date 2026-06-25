from django.contrib import admin
from django.urls import path, include
from .import views

app_name = "fuel"


urlpatterns = [
    #ダッシュボード
    path("", views.dashboard, name="dashboard"),
    #燃費管理
    path("list/", views.record_list, name="record_list"),
    path("add/", views.record_add, name="record_add"),
    path("<int:pk>/", views.record_detail, name="record_detail"),
    path("<int:pk>/edit/", views.record_edit, name="record_edit"),
    #オイル交換管理での追加
    path("maintenance/add/", views.maintenance_add, name="maintenance_add"), 
    path("maintenance/",  views.maintenance_list, name="maintenance_list"), 
    ]   