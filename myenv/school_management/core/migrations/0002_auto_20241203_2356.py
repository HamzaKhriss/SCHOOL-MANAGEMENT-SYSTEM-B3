from django.contrib.auth.models import Group, Permission
from django.db import migrations

def create_groups(apps, schema_editor):
    # Get or create groups
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    teacher_group, _ = Group.objects.get_or_create(name='Teacher')
    student_group, _ = Group.objects.get_or_create(name='Student')

    # Assign permissions to groups
    admin_permissions = Permission.objects.all()  # Admin gets all permissions
    admin_group.permissions.set(admin_permissions)

    teacher_permissions = Permission.objects.filter(codename__in=[
        'view_class', 'add_grade', 'change_grade', 'view_grade'
    ])
    teacher_group.permissions.set(teacher_permissions)

    student_permissions = Permission.objects.filter(codename__in=[
        'view_grade'
    ])
    student_group.permissions.set(student_permissions)

def delete_groups(apps, schema_editor):
    # Remove groups if the migration is rolled back
    Group.objects.filter(name__in=['Admin', 'Teacher', 'Student']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  # Update with your latest auth migration
        ('core', '0001_initial'),  # Replace with the latest migration in your app
    ]

    operations = [
        migrations.RunPython(create_groups, reverse_code=delete_groups),
    ]
