# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20141119_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shorturl',
            options={'verbose_name': 'Short URL'},
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='original',
            field=models.URLField(unique=True, max_length=2000),
            preserve_default=True,
        ),
    ]
