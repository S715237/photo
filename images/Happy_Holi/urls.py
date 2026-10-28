from django.urls import path
from . import views
urlpatterns = [
    path('holi/', views.holi_view, name='holi')
]