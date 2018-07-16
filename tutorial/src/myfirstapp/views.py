from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import First

# Create your views here.


class FirstAppView(viewsets.ModelViewSet):

    comment = "This is my first app"

    # def get(self, request):
    #     return HttpResponse(self.comment)

# for customising do  thi
# writet qyery set
