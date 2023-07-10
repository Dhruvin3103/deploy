from django.urls import path
from .views import PortfolioAPI,ContactusAPI,SlaveAPI,SearchAPI,Search2API

urlpatterns = [
    path('portfolio/', PortfolioAPI.as_view()),
    path('contactus/',ContactusAPI.as_view()),
    # path('slave/',SlaveAPI.as_view()),
    path('search/',SearchAPI.as_view()),
    path('search2/',Search2API.as_view()),
]