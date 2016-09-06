# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20160906_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='instructor',
            field=models.ForeignKey(default=1, to='student.Instructor'),
        ),
    ]
