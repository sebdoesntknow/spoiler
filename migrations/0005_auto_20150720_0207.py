# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_spoiler', '0004_auto_20150720_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spoiler',
            name='tinyurl',
            field=models.URLField(default='None yet', blank=True, max_length=50),
        ),
    ]
