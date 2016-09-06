# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='extension_name',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ManyToManyField(to='student.Student'),
        ),
    ]
