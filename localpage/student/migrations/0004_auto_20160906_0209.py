# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20160906_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='units',
        ),
        migrations.AddField(
            model_name='subject',
            name='lab_units',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='lec_units',
            field=models.IntegerField(default=0),
        ),
    ]
