from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status
from classroom.models import Standard,Student,Test,Marks,Attendance,Subjects,Message
from classroom.serializers import StandardSerializer,\
                                    StudentSerializer,\
                                        TestSerializer,\
                                            MarksSerializer,\
                                                AttendanceSerializer,\
                                                    UserSerializer,\
                                                        SubjectSerializer,MessageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from classroom.permitions import IsAdminOrReadPermission
from django.contrib.auth.models import User

# Create your views here.
class UserApiView(ListCreateAPIView):
    serializer_class=UserSerializer
    def list(self,request):
        user=self.serializer_class(request.user)
        if not request.user.is_staff:
            user=StudentSerializer(Student.objects.filter(user=request.user).first())
        return Response(user.data) 
        
class StandardApiView(ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer
    filter_backends = [DjangoFilterBackend]

class SubjectApiView(ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['standard']

class StudentApiView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['standard','user__username']

    def perform_destroy(self,instance):
        User.objects.get(id=instance.user.id).delete()
        return instance

    @action(detail=False, methods=['post'])
    def deposite_fee(self,request:Request):
        stuId=request.data["studentId"]
        amount=request.data["amount"]
        student = self.queryset.filter(id=stuId).first()
        student.fee_left=max(student.fee_left-amount,0)
        student.save()
        return Response(data={"ok":"ok"},status=status.HTTP_200_OK)

class MarksApiView(ModelViewSet):
    queryset=Marks.objects.all().order_by('-test__date')
    serializer_class = MarksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['test','student']

class TestApiView(ModelViewSet):
    queryset = Test.objects.all().order_by('-date')
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject','standard']

class MessageApiView(ModelViewSet):
    queryset = Message.objects.all().order_by('-date_time')
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['standard']

class AttendanceApiView(ModelViewSet):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student']

    @action(detail=False, methods=['post'])
    def create_many(self,request:Request):
        students = list(map(lambda v: {'student':v},request.data['students']))
        for s in students:
            serializer = self.get_serializer_class()
            attendence =  serializer(data=s)
            if attendence.is_valid():
                attendence.save()
        return Response(data={"ok":"ok"},status=status.HTTP_201_CREATED)