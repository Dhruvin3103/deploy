from django.shortcuts import render
from .models import Portfolio,Contactus
from .serializer import PortfolioSerializer,ContactusSerializer
from  rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
# Create your views here.

class PortfolioAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class ContactusAPI(GenericAPIView, CreateModelMixin):
    serializer_class = ContactusSerializer
    queryset = Contactus.objects.all()
    def post(self, request):
        return self.create(request)