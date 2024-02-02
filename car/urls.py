from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.carDetailsView.as_view(), name='car_details'),
    path('buy/<int:id>/', views.BuyCar, name='buy_car')
]
