from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Standard(models.Model):
    name=models.CharField(max_length=20)
    @property
    def student_count(self):
        return self.students.count()
    def __str__(self):
        return self.name

class Subjects(models.Model):
    name=models.CharField(max_length=50)
    material_url=models.TextField()
    standard=models.ForeignKey(Standard,on_delete=models.CASCADE,related_name='subjects',null=True)

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
    roll_number=models.PositiveIntegerField()
    name=models.CharField(max_length=50)
    standard=models.ForeignKey(Standard,on_delete=models.SET_NULL,related_name='students',null=True)
    dob=models.CharField(max_length=20)
    monther_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=15)
    address=models.TextField()
    gender=models.CharField(max_length=10)
    fee_left=models.PositiveIntegerField()
    total_fee=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.roll_number} - {self.name} - {self.user.email}"

class Test(models.Model):
    name=models.CharField(max_length=50)
    subject=models.ForeignKey(Subjects,on_delete=models.SET_NULL,null=True)
    standard=models.ForeignKey(Standard,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)
    total_marks=models.PositiveIntegerField()

class Marks(models.Model):
    test=models.ForeignKey(Test,on_delete=models.CASCADE,related_name='student_marks')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    marks_got=models.PositiveIntegerField()

    class Meta:
        unique_together = (('test', 'student'),)

class Attendance(models.Model):
    date=models.DateField(auto_now_add=True,editable=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        unique_together = (('date', 'student'),)

class Message(models.Model):
    standard=models.ForeignKey(Standard,on_delete=models.CASCADE)
    message=models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)