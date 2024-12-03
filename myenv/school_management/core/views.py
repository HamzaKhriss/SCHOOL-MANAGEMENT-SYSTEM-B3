from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.forms import modelformset_factory  # Add this import
from .models import Student, Class, Subject, Grade, Attendance, Teacher
from .forms import StudentForm, ClassForm, SubjectForm, GradeForm, AttendanceForm, TeacherForm
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from .models import Grade, Student
from .models import Subject
from .forms import SubjectForm

@login_required
def index(request):
    is_teacher = request.user.groups.filter(name='Teacher').exists()
    is_student = request.user.groups.filter(name='Student').exists()
    return render(request, 'core/index.html', {
        'is_teacher': is_teacher,
        'is_student': is_student,
    })
# Student Views
@login_required
@permission_required('core.add_student', raise_exception=True)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

@login_required
@permission_required('core.change_student', raise_exception=True)
def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form})

@login_required
@permission_required('core.delete_student', raise_exception=True)
def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/student_confirm_delete.html', {'student': student})

@login_required
@permission_required('core.view_student', raise_exception=True)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

@login_required
@permission_required('core.view_student', raise_exception=True)
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'core/student_detail.html', {'student': student})

# Class Views
@login_required
@permission_required('core.add_class', raise_exception=True)
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'core/class_form.html', {'form': form})

@login_required
@permission_required('core.change_class', raise_exception=True)
def class_update(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=class_instance)
    return render(request, 'core/class_form.html', {'form': form})

@login_required
@permission_required('core.delete_class', raise_exception=True)
def class_delete(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        class_instance.delete()
        return redirect('class_list')
    return render(request, 'core/class_confirm_delete.html', {'class': class_instance})

@login_required
@permission_required('core.view_class', raise_exception=True)
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'core/class_list.html', {'classes': classes})

@login_required
@permission_required('core.view_class', raise_exception=True)
def class_detail(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    return render(request, 'core/class_detail.html', {'class': class_instance})

# Subject Views
@login_required
@permission_required('core.add_subject', raise_exception=True)
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'core/subject_form.html', {'form': form})

@login_required
@permission_required('core.change_subject', raise_exception=True)
def subject_update(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'core/subject_form.html', {'form': form})

@login_required
@permission_required('core.delete_subject', raise_exception=True)
def subject_delete(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'core/subject_confirm_delete.html', {'subject': subject})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'core/subject_list.html', {'subjects': subjects})

@login_required
@permission_required('core.view_subject', raise_exception=True)
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'core/subject_detail.html', {'subject': subject})

# Grade Views
@login_required
def grade_list(request):
    # Get the Student instance associated with the logged-in user
    student = get_object_or_404(Student, user=request.user)
    # Filter grades based on the Student instance
    grades = Grade.objects.filter(student_id=student)
    return render(request, 'core/grade_list.html', {'grades': grades})

@login_required
@permission_required('auth.change_user', raise_exception=True)
def assign_user_to_group(request, user_id, group_name):
    user = User.objects.get(id=user_id)
    group = Group.objects.get(name=group_name)
    user.groups.add(group)
    user.save()
    return redirect('index')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
@permission_required('core.view_grade', raise_exception=True)
def grade_detail(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    return render(request, 'core/grade_detail.html', {'grade': grade})

@login_required
@permission_required('core.add_grade', raise_exception=True)
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'core/grade_form.html', {'form': form})

@login_required
@permission_required('core.change_grade', raise_exception=True)
def grade_update(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'core/grade_form.html', {'form': form})

@login_required
@permission_required('core.delete_grade', raise_exception=True)
def grade_delete(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'core/grade_confirm_delete.html', {'grade': grade})

# Attendance Views
@login_required
@permission_required('core.view_attendance', raise_exception=True)
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'core/attendance_list.html', {'attendances': attendances})

@login_required
@permission_required('core.view_attendance', raise_exception=True)
def attendance_detail(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    return render(request, 'core/attendance_detail.html', {'attendance': attendance})

@login_required
@permission_required('core.add_attendance', raise_exception=True)
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'core/attendance_form.html', {'form': form})

@login_required
@permission_required('core.change_attendance', raise_exception=True)
def attendance_update(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'core/attendance_form.html', {'form': form})

@login_required
@permission_required('core.delete_attendance', raise_exception=True)
def attendance_delete(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'core/attendance_confirm_delete.html', {'attendance': attendance})

@login_required
@permission_required('core.add_attendance', raise_exception=True)
def class_attendance(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    students = Student.objects.filter(class_id=class_instance)
    AttendanceFormSet = modelformset_factory(Attendance, form=AttendanceForm, extra=len(students))

    if request.method == 'POST':
        formset = AttendanceFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.class_id = class_instance
                instance.save()
            update_grades_based_on_attendance()
            return redirect('attendance_list')
    else:
        initial_data = [{'student_id': student, 'class_id': class_instance} for student in students]
        formset = AttendanceFormSet(queryset=Attendance.objects.none(), initial=initial_data)

    return render(request, 'core/class_attendance.html', {'formset': formset, 'class_instance': class_instance})

# Teacher Views
@login_required
@permission_required('core.view_teacher', raise_exception=True)
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/teacher_list.html', {'teachers': teachers})

@login_required
@permission_required('core.view_teacher', raise_exception=True)
def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'core/teacher_detail.html', {'teacher': teacher})

@login_required
@permission_required('core.add_teacher', raise_exception=True)
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'core/teacher_form.html', {'form': form})

@login_required
@permission_required('core.change_teacher', raise_exception=True)
def teacher_update(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'core/teacher_form.html', {'form': form})

@login_required
@permission_required('core.delete_teacher', raise_exception=True)
def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'core/teacher_confirm_delete.html', {'teacher': teacher})

# Additional Views
@login_required
@permission_required('core.view_attendance', raise_exception=True)
def attendance_report(request):
    return render(request, 'attendance/report.html')

@login_required
@permission_required('core.view_grade', raise_exception=True)
def grade_report(request):
    students = Student.objects.all()
    student_grades = []

    for student in students:
        grades = Grade.objects.filter(student_id=student)
        student_grades.append({
            'student': student,
            'grades': grades
        })

    context = {
        'student_grades': student_grades
    }

    return render(request, 'grades/report.html', context)

@login_required
@permission_required('auth.change_user', raise_exception=True)
def assign_user_to_group(user_id, group_name):
    user = User.objects.get(id=user_id)
    group = Group.objects.get(name=group_name)
    user.groups.add(group)
    user.save()

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')