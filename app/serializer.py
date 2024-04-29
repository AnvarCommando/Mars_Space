from rest_framework import serializers
from .models import *

class Registersrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class TeachersSRL(serializers.ModelSerializer):
    class  Meta:
        model = Teacher
        "__fields__"

class GroupSRL(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class StudentSRL(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentSRL(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'lastname', 'phone', 'password']


class DavomatSRL(serializers.ModelSerializer):
    class Meta:
        model = davomat
        fields = "__all__"

class HomeSRL(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'
        
class HackatonSRL(serializers.ModelSerializer):
    class Meta:
        model = Hackaton
        fields = '__all__'