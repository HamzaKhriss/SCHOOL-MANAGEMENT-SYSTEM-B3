from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:student_id>/edit/', views.student_update, name='student_update'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
    
    # URLs for Teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:teacher_id>/edit/', views.teacher_update, name='teacher_update'),
    path('teachers/<int:teacher_id>/delete/', views.teacher_delete, name='teacher_delete'),

    # URLs for Class
    path('classes/', views.class_list, name='class_list'),
    path('classes/<int:class_id>/', views.class_detail, name='class_detail'),
    path('classes/create/', views.class_create, name='class_create'),
    path('classes/<int:class_id>/edit/', views.class_update, name='class_update'),
    path('classes/<int:class_id>/delete/', views.class_delete, name='class_delete'),

    # URLs for Subject
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('subjects/<int:subject_id>/edit/', views.subject_update, name='subject_update'),
    path('subjects/<int:subject_id>/delete/', views.subject_delete, name='subject_delete'),


    path('grades/', views.grade_list, name='grade_list'),
    path('assign_user_to_group/<int:user_id>/<str:group_name>/', views.assign_user_to_group, name='assign_user_to_group'),
    path('logout/', views.logout_view, name='logout'),
    path('grades/<int:grade_id>/', views.grade_detail, name='grade_detail'),
    path('grades/create/', views.grade_create, name='grade_create'),
    path('grades/<int:grade_id>/edit/', views.grade_update, name='grade_update'),
    path('grades/<int:grade_id>/delete/', views.grade_delete, name='grade_delete'),
    path('grades/report/', views.grade_report, name='grade_report'),

    # URLs for Attendance
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/<int:attendance_id>/edit/', views.attendance_update, name='attendance_update'),
    path('attendance/<int:attendance_id>/delete/', views.attendance_delete, name='attendance_delete'),
    path('attendance/class/<int:class_id>/', views.class_attendance, name='class_attendance'),
    path('attendance/report/', views.attendance_report, name='attendance_report'),

    path('admin/', admin.site.urls),

]