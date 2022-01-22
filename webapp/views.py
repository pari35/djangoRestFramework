
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sqlalchemy import true
from .models import employees
from .serializers import employeesSerializer


class employeList(APIView):
    def get(self,request):
        emp =employees.objects.all()
        serializer =employeesSerializer(emp,many=True)
        return Response(serializer.data)

    def post(self):
        pass



# Create your views here.

