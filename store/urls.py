from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/', views.removeItemFromCart),
    path('cart/checkout/', views.checkout),
    path('cart/checkout/complete/', views.submitOrder),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin'),


]

