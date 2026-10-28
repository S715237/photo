from django.urls import path
from . import views

urlpatterns = [
    path('morning/', views.morning_gallery, name='morning'),
]