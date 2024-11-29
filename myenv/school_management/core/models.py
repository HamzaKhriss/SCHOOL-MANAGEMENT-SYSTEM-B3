from django.db import models


class Student(models.Model):
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
        ]
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()

class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)