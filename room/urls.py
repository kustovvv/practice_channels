from django.urls import path

from . import views

app_name = 'room'

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<str:slug>/', views.details, name='details'),
]