from django.shortcuts import render
from .seriializer import StudentSerializer
from rest_framework import viewsets
from  .models import Student
from rest_framework.authentication import SessionAuthentication
from .custom_permisson import Mypermissions 



class StudentModelviewsApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Mypermissions]
