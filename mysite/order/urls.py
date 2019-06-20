from django.urls import path

from order import views

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetails.as_view()),
    path('orders/<int:pk>/items/', views.OrderItemList.as_view()),
    path('orders/<int:pk1>/items/<int:pk2>/', views.OrderItemDetail.as_view())
]