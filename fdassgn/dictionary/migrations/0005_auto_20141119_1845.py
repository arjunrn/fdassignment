# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_auto_20141119_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='word',
        ),
        migrations.DeleteModel(
            name='ShortURL',
        ),
        migrations.AddField(
            model_name='dictword',
            name='URL',
            field=models.URLField(verbose_name='Full URL', max_length=2000, db_index=True, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictword',
            name='ts',
            field=models.DateTimeField(null=True, default=None),
            preserve_default=True,
        ),
    ]
