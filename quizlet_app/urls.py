from django.urls import path
from . import views

urlpatterns = [
    path('create-deck/', views.create_deck, name='create_deck'),
    path('deck/<int:deck_id>/', views.view_deck, name='view_deck'),
    path('deck/<int:deck_id>/add-flashcard/', views.add_flashcard, name='add_flashcard'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # Add more URL patterns as needed for your app
]
