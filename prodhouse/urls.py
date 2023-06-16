from django.urls import path
from .views import PortfolioAPI,ContactusAPI,SlaveAPI

urlpatterns = [
    path('portfolio/', PortfolioAPI.as_view()),
    path('contactus/',ContactusAPI.as_view()),
    path('slave/',SlaveAPI.as_view()),
]