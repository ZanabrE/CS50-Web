from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.desconocido, name="desconocido"),
    path("greet", views.greet, name="greet"),
    path("saludos", views.saludos, name="saludos")
]
