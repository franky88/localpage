# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20160906_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectschedule',
            name='end_time',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='subjectschedule',
            name='time_start',
            field=models.CharField(max_length=8),
        ),
    ]
