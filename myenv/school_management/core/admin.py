from django.contrib import admin
from .models import Student, Teacher, Class, Subject, Grade, Attendance, User

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(User)