from  rest_framework import serializers
from classroom.models import Student,Standard,Test,Marks,Attendance,Subjects,Message
from django.contrib.auth.models import User

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Standard
        fields=(
            'id',
            'name',
            'student_count'
        )

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    name=serializers.CharField(source="first_name", read_only=True)
    password=serializers.CharField(write_only=True)
    username=serializers.CharField(write_only=True)
    first_name=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=(
            'id',
            'username',
            'name',
            'first_name',
            'password',
            'email',
            'is_staff'
        )
    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    email=serializers.CharField(source='user.email')
    password=serializers.CharField(source='user.password',write_only=True)
    standard_data=StandardSerializer(source='standard', read_only=True)
    is_staff=serializers.BooleanField(source='user.is_staff', read_only=True)
    class Meta:
        model=Student
        # fields='__all__'
        exclude = ['user']

    def create(self,validated_data):
        email=validated_data['user']['email']
        password=validated_data['user']['password']
        user = User(username=email,email=email)
        user.set_password(password)
        user.save()
        validated_data["user"]=user
        return  Student.objects.create(**validated_data);

class MarksSerializer(serializers.ModelSerializer):
    student_data=StudentSerializer(source='student',read_only=True)
    test_name=serializers.CharField(source='test.name',read_only=True)
    date = serializers.DateTimeField(source='test.date',read_only=True)
    total_marks =serializers.IntegerField(source='test.total_marks',read_only=True)
    class Meta:
        model=Marks
        fields=(
            'id',
            'test',
            'student',
            'marks_got',
            'student_data',
            'test_name',
            'date',
            'total_marks'
        )

class TestSerializer(serializers.ModelSerializer):
    subject_name=serializers.CharField(source="subject.name",read_only=True)
    class Meta:
        model=Test
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'
