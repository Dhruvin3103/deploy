from django.shortcuts import render
from .models import Portfolio
from .serializer import PortfolioSerializer
from  rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
# Create your views here.

class PortfolioAPI(GenericAPIView, ListModelMixin):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
    def get(self, request):
        return self.list(request)