from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from .models import Student, Teacher, Class, Subject, Grade, Attendance
from .forms import StudentForm, TeacherForm, ClassForm, SubjectForm, GradeForm, AttendanceForm



def index(request):
    return render(request, 'core/index.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'core/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

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

def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/student_confirm_delete.html', {'student': student})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'core/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'core/teacher_form.html', {'form': form})

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

def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'core/teacher_confirm_delete.html', {'teacher': teacher})

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'core/class_list.html', {'classes': classes})

def class_detail(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    return render(request, 'core/class_detail.html', {'class': class_instance})

def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'core/class_form.html', {'form': form})

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

def class_delete(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        class_instance.delete()
        return redirect('class_list')
    return render(request, 'core/class_confirm_delete.html', {'class': class_instance})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'core/subject_list.html', {'subjects': subjects})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'core/subject_detail.html', {'subject': subject})

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'core/subject_form.html', {'form': form})

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

def subject_delete(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'core/subject_confirm_delete.html', {'subject': subject})

# Views for Grade
def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'core/grade_list.html', {'grades': grades})

def grade_detail(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    return render(request, 'core/grade_detail.html', {'grade': grade})

def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'core/grade_form.html', {'form': form})

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

def grade_delete(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'core/grade_confirm_delete.html', {'grade': grade})
def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'core/attendance_list.html', {'attendance_records': attendance_records})

def attendance_detail(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    return render(request, 'core/attendance_detail.html', {'attendance': attendance})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            update_grades_based_on_attendance()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'core/attendance_form.html', {'form': form})

def attendance_update(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            update_grades_based_on_attendance()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'core/attendance_form.html', {'form': form})

def attendance_delete(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        update_grades_based_on_attendance()
        return redirect('attendance_list')
    return render(request, 'core/attendance_confirm_delete.html', {'attendance': attendance})

def update_grades_based_on_attendance():
    students = Student.objects.all()
    for student in students:
        total_absences = Attendance.objects.filter(student_id=student, status='Absent').count()
        grades = Grade.objects.filter(student_id=student)
        for grade in grades:
            grade.marks = max(0, grade.marks - total_absences)
            grade.save()

# View for managing attendance for all students in a class
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

from django.shortcuts import render
from .models import Student, Grade

def update_grades_based_on_attendance():
    students = Student.objects.all()
    for student in students:
        total_absences = Attendance.objects.filter(student_id=student, status='Absent').count()
        grades = Grade.objects.filter(student_id=student)
        for grade in grades:
            grade.marks = max(0, grade.marks - total_absences)
            grade.save()

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
def attendance_report(request):
    # Your logic here
    return render(request, 'attendance/report.html')