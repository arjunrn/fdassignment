# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20141119_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictword',
            name='url',
        ),
        migrations.AddField(
            model_name='shorturl',
            name='word',
            field=models.ForeignKey(to='dictionary.DictWord', default=None, unique=True),
            preserve_default=False,
        ),
    ]
