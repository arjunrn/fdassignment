# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('original', models.CharField(unique=True, max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='dictword',
            options={'verbose_name': 'Dictionary Word'},
        ),
        migrations.RemoveField(
            model_name='dictword',
            name='used',
        ),
        migrations.AddField(
            model_name='dictword',
            name='url',
            field=models.ForeignKey(default=None, null=True, to='dictionary.ShortURL'),
            preserve_default=True,
        ),
    ]
