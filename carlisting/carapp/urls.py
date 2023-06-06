
from django.contrib import admin
from django.urls import path, include
from carapp import views

urlpatterns = [
    path("", views.index),
    path("list-car/", views.car_listing),
    path('thank-you/<int:car_id>/', views.thank_you, name='thank_you'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('car/list/', views.car_list, name='car_list'),
    path('buy/<int:car_id>/', views.buy_form, name='buy_form'),
    path('success/<int:car_id>/', views.success_page, name='success'),

]
