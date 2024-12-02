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
            models.Index(fields=['class_id']),
        ]

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

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['teacher_id']),
        ]

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    credits = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

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

class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      role = models.CharField(max_length=50)
    
      def __str__(self):
        return self.user.username