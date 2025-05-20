from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ernesto", views.ernesto, name="ernesto"),
    path("greet", views.greet, name="greet"),
    path("saludos", views.saludos, name="saludos")
]
