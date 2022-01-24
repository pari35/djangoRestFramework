from unicodedata import name
from rest_framework import serializers

# from .views import student_api
from .models import student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=10) 

def create(self,validated_data):
    return student.objects.create(**validated_data)

def update(self,instance,validated_data):
    print(instance.name)
    instance.name=validated_data.get('name',instance.name)
    print(instance.name)
    instance.roll=validated_data.get('roll',instance.roll)
    instance.city=validated_data.get('city',instance.city)
    instance.save()
    return instance