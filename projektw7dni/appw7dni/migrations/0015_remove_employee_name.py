# Generated by Django 4.0.3 on 2022-06-19 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appw7dni', '0014_hourtableend_building_hourtablestart_building'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
    ]
