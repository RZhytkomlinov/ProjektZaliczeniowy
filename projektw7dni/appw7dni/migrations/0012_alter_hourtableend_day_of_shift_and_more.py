# Generated by Django 4.0.3 on 2022-06-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appw7dni', '0011_alter_hourtableend_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourtableend',
            name='day_of_shift',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='hourtablestart',
            name='day_of_shift',
            field=models.DateField(null=True),
        ),
    ]
