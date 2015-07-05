# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_spoiler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spoiler',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('spoiler_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='Date Added')),
                ('votes', models.IntegerField(default=0)),
                ('title', models.ForeignKey(to='web_spoiler.Title')),
            ],
        ),
    ]
