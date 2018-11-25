from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('logout/', views.logout),
    path('register/', views.register),

    path('orders/', views.order_list),
    path('orders/create/', views.OrderCreate.as_view()),
    path('<int:pk>/', views.OrderDetails.as_view()),
    path('orders/<int:pk>/', views.OrDetailView.as_view()),

    path('restaurants/', views.restaurant_list),
    path('restaurants/create/', views.RestaurantCreate.as_view()),
    path('<int:pk>/', views.RestaurantDetails.as_view()),
    path('restaurants/<int:pk>/', views.ResDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)