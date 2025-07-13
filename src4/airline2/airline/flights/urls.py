from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>/', views.detail, name='detail'),
    path('<int:flight_id>/book/', views.book, name='book'),
]