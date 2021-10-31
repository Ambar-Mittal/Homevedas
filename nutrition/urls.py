from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="Home"),
    path("about/",views.about, name="AboutUs"),
    path("fruits/",views.fruit, name="Fruits"),
    path("dairy/",views.dairy, name="Dairy"),
    path("spices/",views.spices, name="Spices"),
    path("search/",views.search, name="Search"),
    path("vegetables/",views.vegetables, name="Vegetables"),
]
