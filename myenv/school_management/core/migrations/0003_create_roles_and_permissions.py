# migrations/0003_create_roles_and_permissions.py

from django.db import migrations

def create_roles_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Create groups
    admin_group, created = Group.objects.get_or_create(name='Admin')
    teacher_group, created = Group.objects.get_or_create(name='Teacher')
    student_group, created = Group.objects.get_or_create(name='Student')

    # Assign permissions to groups
    if created:
        # Admin permissions
        admin_permissions = Permission.objects.all()
        admin_group.permissions.set(admin_permissions)

        # Teacher permissions
        teacher_permissions = Permission.objects.filter(codename__in=[
            'add_grade', 'change_grade', 'view_grade',
            'add_attendance', 'change_attendance', 'view_attendance'
        ])
        teacher_group.permissions.set(teacher_permissions)

        # Student permissions
        student_permissions = Permission.objects.filter(codename__in=[
            'view_grade', 'view_attendance'
        ])
        student_group.permissions.set(student_permissions)

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),  # Adjust this dependency to match your project
        ('core', '0002_remove_grade_grade_alter_class_name_and_more'),  # Replace with the latest migration file in your core app
    ]

    operations = [
        migrations.RunPython(create_roles_and_permissions),
    ]