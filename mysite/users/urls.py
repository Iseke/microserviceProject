from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view())
]