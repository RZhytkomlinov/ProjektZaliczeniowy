# Generated by Django 4.0.3 on 2022-06-19 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appw7dni', '0018_employee_email_employee_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
    ]
