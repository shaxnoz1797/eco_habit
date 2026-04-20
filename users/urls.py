from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_habits, name='my_habits'),  # 👈 HOME SHU
    path('add/', views.add_habit, name='add_habit'),
    path('edit/<int:pk>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:pk>/', views.delete_habit, name='delete_habit'),
    path('toggle/<int:pk>/', views.toggle_habit, name='toggle_habit'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('api/habit/<int:pk>/done/', views.api_update_habit, name='api_done'),


]