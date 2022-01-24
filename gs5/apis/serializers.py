from unicodedata import name
from wsgiref.validate import validator
from rest_framework import serializers

# from .views import student_api
from .models import student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10,validators=[start_with_r])
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


#field level validation
def validate_roll(self,value):
    if value >=200:
        raise serializers.ValidationError('Seat Full')
    return value

#object level validation
def validate(self,data):
    nm=data.get('name')
    ct=data.get('city')
    if nm.lower()=='rohit' and ct.lower()!='ranchi':
        raise serializers.ValidationError('city must be ranchi')
    return


#validators
def start_with_r(value):
    if value[0].lower()!= 'r':
        raise serializers.ValidationError('Name should start with r')
