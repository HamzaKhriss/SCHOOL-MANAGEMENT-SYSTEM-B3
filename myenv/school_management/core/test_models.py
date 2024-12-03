import django
from django.conf import settings
from django.db import models
from django.core.management import call_command
from django.test import TestCase
from core.models import Student, Teacher, Class, Subject, Grade, Attendance
from django.contrib.auth.models import User

# Initialize Django settings
settings.configure(
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'core',  # Assuming your app is named 'core'
        'django.contrib.admin',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_db.sqlite3',
        }
    },
    USE_TZ=True,
    TIME_ZONE='UTC',
)

# Initialize Django
django.setup()

# Test if Django models are working correctly
class ModelTestCase(TestCase):

    def setUp(self):
        # Create a user for Student
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create Teacher
        self.teacher = Teacher.objects.create(
            name='Test Teacher',
            subject='Mathematics',
            contact_number='1234567890'
        )

        # Create Class
        self.class_obj = Class.objects.create(
            name='Class 1',
            teacher_id=self.teacher
        )

        # Create Student
        self.student = Student.objects.create(
            user=self.user,
            name='Test Student',
            dob='2000-01-01',
            address='123 Street',
            contact_number='9876543210',
            class_id=self.class_obj
        )

        # Create Subject
        self.subject = Subject.objects.create(
            name='Math',
            teacher=self.teacher
        )

        # Create Grade
        self.grade = Grade.objects.create(
            student_id=self.student,
            subject_id=self.subject,
            marks=85
        )

        # Create Attendance
        self.attendance = Attendance.objects.create(
            student_id=self.student
        )

    def test_student_creation(self):
        # Test that the student was created successfully
        student = Student.objects.get(pk=self.student.student_id)
        self.assertEqual(student.name, 'Test Student')
        self.assertEqual(student.class_id.name, 'Class 1')

    def test_teacher_creation(self):
        # Test that the teacher was created successfully
        teacher = Teacher.objects.get(pk=self.teacher.teacher_id)
        self.assertEqual(teacher.name, 'Test Teacher')
        self.assertEqual(teacher.subject, 'Mathematics')

    def test_class_creation(self):
        # Test that the class was created successfully
        class_obj = Class.objects.get(pk=self.class_obj.class_id)
        self.assertEqual(class_obj.name, 'Class 1')
        self.assertEqual(class_obj.teacher_id.name, 'Test Teacher')

    def test_subject_creation(self):
        # Test that the subject was created successfully
        subject = Subject.objects.get(pk=self.subject.id)
        self.assertEqual(subject.name, 'Math')
        self.assertEqual(subject.teacher.name, 'Test Teacher')

    def test_grade_creation(self):
        # Test that the grade was created successfully
        grade = Grade.objects.get(pk=self.grade.grade_id)
        self.assertEqual(grade.marks, 85)
        self.assertEqual(grade.student_id.name, 'Test Student')

    def test_attendance_creation(self):
        # Test that the attendance was created successfully
        attendance = Attendance.objects.get(pk=self.attendance.attendance_id)
        self.assertEqual(attendance.student_id.name, 'Test Student')

    def test_student_update(self):
        # Test updating a student
        self.student.name = 'Updated Student'
        self.student.save()
        updated_student = Student.objects.get(pk=self.student.student_id)
        self.assertEqual(updated_student.name, 'Updated Student')

    def test_delete_student(self):
        # Test deleting a student
        student_id = self.student.student_id
        self.student.delete()
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(pk=student_id)

    def test_querying(self):
        # Test if querying works correctly
        student = Student.objects.get(pk=self.student.student_id)
        self.assertEqual(student.class_id.name, 'Class 1')

if __name__ == '__main__':
    # Run the tests
    call_command('test', 'core')  # Replace 'core' with your app name
