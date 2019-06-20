from django.urls import path

from shop import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetails.as_view()),
    path('categories/<int:pk>/products/', views.ProductList.as_view()),
    path('categories/<int:pk1>/products/<int:pk2>/', views.ProductDetail.as_view())

]