from functools import partial
import json
from django import views
from django.shortcuts import render
import io
from pandas import json_normalize
from parso import parse
from rest_framework.parsers import JSONParser
from sqlalchemy import true

from .models import student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class studentAPI(view):
    def get(self,request,*args, **kwargs):
        if request.method == 'GET':
            json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu = student.objects.get(id=id)
            serialiser =StudentSerializer(stu)
            json_data =JSONRenderer().render(serialiser.data)
            return HttpResponse(json_data, content_type='application/json')


def post(self,request,*args, **kwargs):
    json_data=request.body
    stream =io.BytesIO(json_data)
    pythondata=JSONParser().parse(stream)
    serialiser =StudentSerializer(data=pythondata)
    if serialiser.is_valid():
        serialiser.save()
        res={'msg':'Data Created'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    json_data=JSONRenderer().render(serialiser.errors)
    return HttpResponse(json_data,content_type='application/json')

def put(self,request,*args, **kwargs):
    json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=student.objects.create(id=id)
        serialiser=StudentSerializer(stu,data=pythondata,partial=True)
    if serialiser.is_valid():
        serialiser.save()
        res={'msg':'Data updated !!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')


def delete(self,request,*args, **kwargs):
    json_data=request.body
    stream=io.BytesIO()(json_data)
    pyythondata=JSONParser().parse(stream)
    id=pyythondata.get('id')
    stu=student.objects.get(id=id)
    stu.delete()
    res={'msg':'data deleted'}
    # json_data=JSONRenderer().render(res)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(res)