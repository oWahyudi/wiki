from django.urls import path


from . import views

app_name="encyclopedia"
urlpatterns = [
  
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("randompage", views.randompage, name="randompage"),


    path('<str:undefinedpath>', views.custom_404_view, name="custom_404"),
 
]