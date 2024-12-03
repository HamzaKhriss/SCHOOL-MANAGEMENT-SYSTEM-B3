from django.db import models
from django.contrib.auth.models import User

# In core/models.py
def get_default_user():
    return User.objects.get(id=1) 

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    dob = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)
   
    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['dob']),
            models.Index(fields=['class_id']),
        ]
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    subject = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['subject']),
        ]

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')


class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['student_id']),
            models.Index(fields=['subject_id']),
        ]

    def __str__(self):
        return f"{self.student_id.user.username} - {self.subject_id.name} - {self.marks}"

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)