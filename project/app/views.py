from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import  AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [AllowAny]
	queryset = StudentModel.objects.all()
	serializer_class = StudentSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = EmployeeModel.objects.all()
	serializer_class = EmployeeSerializer
class CarViewSet(viewsets.ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = CarModel.objects.all()
	serializer_class = CarSerializer