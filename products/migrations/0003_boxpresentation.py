# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150505_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxPresentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bottlesize', models.CharField(max_length=20)),
                ('bottles', models.PositiveSmallIntegerField()),
                ('maxlabels', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
