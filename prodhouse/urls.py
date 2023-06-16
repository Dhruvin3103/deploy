from django.urls import path
from .views import PortfolioAPI,ContactusAPI

urlpatterns = [
    path('portfolio/', PortfolioAPI.as_view()),
    path('contactus/',ContactusAPI.as_view()),
]