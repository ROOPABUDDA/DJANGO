from django.shortcuts import render, redirect, HttpResponse
from .models import Employee, Manager
from rest_framework import viewsets
from .serializer import EmployeeSerializer, ManagerSerializer
# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# def create(request):
#     # create
#     return HttpResponse("Create user here")


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
