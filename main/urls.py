from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage),
    path('propertyfeed', views.PropertyFeed),
    path('property/<str:propertyId>/', views.PropertyPage)
]