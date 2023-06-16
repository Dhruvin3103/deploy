from django.shortcuts import render
from .models import Portfolio,Contactus
from .serializer import PortfolioSerializer,ContactusSerializer
from  rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
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
        try:
            subject = 'Some one contacted you!!'
            print(request.data)
            message = f"NAME:{request.data['name']}\nEMAIL:{request.data['email']}\nPHONE:{request.data['phone']}\nMESSAGE:{request.data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['gajjoshi2003@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
        except Exception as e:
            return Response({'status': 403, 'message': 'Sorry Some error has occured', 'error':str(e)})
        return self.create(request)