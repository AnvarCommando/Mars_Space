from rest_framework.views import  APIView
from .serializer import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
import random
# Create your views here.

class RegisterView (APIView):
    def post(self, request):
        serializer = Registersrl(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class LoginView(APIView):
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        user = User.objects.filter(name = name, password=password).first()
        if user:
            return Response('Login success')
        else:
            return Response('Not found such kind of user')


class StudentRegisterView(APIView):
    def post(self, request):
        serializer = StudentSRL(data=request)
        if serializer.is_valid():
            student = serializer.save()
            student.space_id = random.randit(10000, 99999)
            student.save()
            return Response(dict(student))
        else:
            return Response(serializer.errors)
            
class Teacher (APIView):
    def post(self, request):
        serializer = TeachersSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class Group (APIView):
    def post(self, request):
        serializer = GroupSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        



class Student (APIView):

    def post(self, request):
        serializer = StudentSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CreateGroupView(APIView):
    def post(self, request):
        serializers = GroupSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        


class DavomatView(APIView):
    def post(self, request):
        serializers = DavomatSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        





class HomerworkViewTeacher(APIView):
    def post(self, request, id):
        teacher = Group.objects.filter(teacher = id).first()
        if teacher:
            serializers = HomeSRL(data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response("Uyga vazifani yuklash ustozlarga berilgan")
        


class GetHomeworkz(APIView):
    def get(self, request):
        homeworks = Homework.objects.all()
        if homeworks:
            serializers = HomeSRL(homeworks, many = True)
            return Response(serializers.data)
        else:
            return Response("Hozircha uyga vazifa topilmadi")
import datetime
class GetStudentHomework(APIView):
    def get(self, request, id):
        ser = []
        student = Group.objects.filter(student = id).first()
        if student:
            today = datetime.datetime.today
            homeworks = Homework.objects.filter(group = student.group)
            for i in homeworks:
                if i.date + 7 <= today:
                    ser.append(i)
                else:
                    continue
                serializers = HomeSRL(ser, many = True)
                return Response(serializers.data)
            else:
                return Response("Student xato")


class UploadHomeworkStudent(APIView):
    def patch(self, request, id):
        homework = Homework.objects.filter(id=id).first()
        if homework:
            serializers = HomeSRL(instance=homework, data=request.data, partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
            
        else:
            return Response("Not found such kind of homework    ")
        
        
from rest_framework.permissions import AllowAny

class HackatonView(generics.CreateAPIView):
    serializer_class = HackatonSRL
    queryset = Hackaton.objects.all()
    permission_classes = [AllowAny]


class HackatonView(generics.ListAPIView):
    serializer_class = HackatonSRL
    queryset = Hackaton.objects.all()
    permission_classes = [AllowAny]