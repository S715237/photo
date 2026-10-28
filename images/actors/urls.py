from django.urls import path
from .import views

urlpatterns = [
    path('movies/', views.showmoviews, name='movies'),
    path('molly/', views.showmolly, name='molly'),
]