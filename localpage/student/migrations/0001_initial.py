# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('block_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('extension_name', models.CharField(max_length=5, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.ForeignKey(to='student.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_of_school_year', models.CharField(max_length=4)),
                ('end_of_school_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Semister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semister', models.CharField(max_length=15)),
                ('school_year', models.ForeignKey(to='student.SchoolYear')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_number', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('extension_name', models.CharField(max_length=5)),
                ('block', models.ForeignKey(to='student.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_code', models.CharField(max_length=20)),
                ('subject_title', models.CharField(max_length=60)),
                ('units', models.IntegerField(default=3)),
                ('duration', models.IntegerField(default=54)),
                ('student', models.ForeignKey(to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_start', models.TimeField()),
                ('end_time', models.TimeField()),
                ('subject', models.ForeignKey(to='student.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='semister',
            field=models.ForeignKey(to='student.Semister'),
        ),
        migrations.AddField(
            model_name='department',
            name='school_year',
            field=models.ForeignKey(to='student.SchoolYear'),
        ),
        migrations.AddField(
            model_name='block',
            name='module',
            field=models.ForeignKey(to='student.Module'),
        ),
    ]
