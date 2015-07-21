# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_spoiler', '0003_spoiler_tinyurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spoiler',
            name='tinyurl',
            field=models.URLField(max_length=50, blank=True),
        ),
    ]
