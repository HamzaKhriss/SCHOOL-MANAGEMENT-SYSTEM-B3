from django.contrib import admin
from .models import Student, Teacher, Class, Subject, Grade, Attendance

# Remove this line if it exists
# admin.site.register(User)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attendance)