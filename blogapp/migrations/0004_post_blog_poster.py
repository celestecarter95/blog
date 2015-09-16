# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20150915_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_poster',
            field=models.CharField(default=b'Celeste', max_length=200),
        ),
    ]
