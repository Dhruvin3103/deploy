from django.urls import path
from .views import PortfolioAPI

urlpatterns = [
    path('portfolio/', PortfolioAPI.as_view()),
]