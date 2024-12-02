# School Management System

## Overview

The School Management System is a web application built with Django that allows administrators to manage students, teachers, classes, subjects, grades, and attendance. The system provides functionalities for CRUD operations, detailed reports, and role-based access control.

## Features

- **Student Management**:
  - Enrollment (add/update/delete students)
  - Assign students to specific classes
  - Maintain personal details like name, date of birth, address, and contact information

- **Teacher Management**:
  - Manage teacher information (name, subject expertise, contact details)
  - Assign teachers to specific classes and subjects

- **Class Management**:
  - Create and manage class schedules
  - Assign students and teachers to classes

- **Grade Management**:
  - Record and update grades for students across subjects
  - Generate grade reports

- **Attendance Tracking**:
  - Record student attendance for each class or session
  - Generate attendance reports

- **Administration Features**:
  - Define roles (admin, teacher, student) with specific privileges
  - Backup and restore database functionality

## Installation

### Prerequisites

- Python 3.12
- Django 5.1.3
- MySQL

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/wisescream/SCHOOL-MANAGEMENT-SYSTEM-B3/tree/main
   cd school_management
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     .\myenv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source myenv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the database**:

   Edit `school_management/settings.py` to configure the database settings:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'school_management_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Create the MySQL database**:

   ```sql
   CREATE DATABASE school_management_db;
   ```

7. **Run migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

9. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

10. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Role-Based Access Control

1. **Create Groups and Assign Permissions**:

   Use the Django shell to create groups and assign permissions:

   ```python
   from django.contrib.auth.models import Group, Permission
   from core.models import Student, Teacher, Class, Subject, Grade, Attendance

   # Create groups
   admin_group, created = Group.objects.get_or_create(name='Admin')
   teacher_group, created = Group.objects.get_or_create(name='Teacher')
   student_group, created = Group.objects.get_or_create(name='Student')

   # Assign permissions to groups
   admin_permissions = Permission.objects.all()
   teacher_permissions = Permission.objects.filter(content_type__model__in=['student', 'class', 'subject', 'grade', 'attendance'])
   student_permissions = Permission.objects.filter(content_type__model='student')

   admin_group.permissions.set(admin_permissions)
   teacher_group.permissions.set(teacher_permissions)
   student_group.permissions.set(student_permissions)
   ```

2. **Assign Users to Groups**:

   Use the Django shell to assign users to groups:

   ```python
   from django.contrib.auth.models import User, Group

   # Assign a user to the admin group
   admin_user = User.objects.get(username='admin')
   admin_group = Group.objects.get(name='Admin')
   admin_user.groups.add(admin_group)

   # Assign a user to the teacher group
   teacher_user = User.objects.get(username='teacher')
   teacher_group = Group.objects.get(name='Teacher')
   teacher_user.groups.add(teacher_group)

   # Assign a user to the student group
   student_user = User.objects.get(username='student')
   student_group = Group.objects.get(name='Student')
   student_user.groups.add(student_group)
   ```

### Backup and Restore

1. **Backup the database**:

   ```bash
   python manage.py dumpdata > backup.json
   ```

2. **Restore the database**:

   ```bash
   python manage.py loaddata backup.json
   ```

### Detailed Reports

1. **Grade Report**:

   Access the grade report at `http://127.0.0.1:8000/grades/report/`.

2. **Attendance Report**:

   Access the attendance report at `http://127.0.0.1:8000/attendance/report/`.

## Database Schema

### Entities

- `Students` (StudentID, Name, DOB, Address, ContactNumber, ClassID)
- `Teachers` (TeacherID, Name, Subject, ContactNumber)
- `Classes` (ClassID, Name, TeacherID)
- `Subjects` (SubjectID, Name, Credits)
- `Grades` (GradeID, StudentID, SubjectID, Marks, Grade)
- `Attendance` (AttendanceID, StudentID, ClassID, Date, Status)
- `Users` (UserID, Username, Password, Role)

### Relationships

- `Students` → `Classes`: Many-to-One (a student belongs to one class).
- `Teachers` → `Classes`: One-to-Many (a teacher manages multiple classes).
- `Subjects` → `Classes`: Many-to-Many (a class can have multiple subjects, and a subject can belong to multiple classes).
- `Grades` → `Students`, `Subjects`: Many-to-One (each grade is linked to a student and a subject).
- `Attendance` → `Students`, `Classes`: Many-to-One (attendance is recorded per student per class).

### Normalized Database Schema (3NF)

- **1NF**: Each column contains atomic data, and each table has a unique identifier (primary key).
- **2NF**: All non-primary key attributes are functionally dependent on the entire primary key.
- **3NF**: Transitive dependencies are eliminated.

## Technical Choices

### Indexes

- **B-Tree Indexes**: Used for range queries (e.g., finding students born in a specific year).
- **Hash Indexes**: Suitable for exact lookups (e.g., fetching a student by StudentID).

### Partitioning Strategy

- **By Class Year**: Separate tables/partitions for each class year to optimize performance when querying or updating data for a specific cohort.
- **By Department**: If the system scales to include departments (e.g., Science, Arts), partition by department to enhance scalability.
