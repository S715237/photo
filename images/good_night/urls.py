from django.urls import path
from . import views
urlpatterns = [
    path('night/', views.good_night_view, name='good_night'),
    path('diwali/',views.diwali_views,name='diwali'),
    path('krishna/', views.krishna_view, name='krishna'),
    path('ganesh/', views.ganesh_view, name='ganesh'),
    path('navratri/', views.navratri_view, name='navratri'),
    path('christmas/', views.christmas_view, name='christmas'),
    path('showform/', views.showform, name='showform'),

]