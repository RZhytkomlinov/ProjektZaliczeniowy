# Generated by Django 4.0.3 on 2022-06-18 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appw7dni', '0005_hourtable_day_of_shift_alter_hourtable_end_of_shift_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourtable',
            name='end_of_shift',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='hourtable',
            name='start_of_shift',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
