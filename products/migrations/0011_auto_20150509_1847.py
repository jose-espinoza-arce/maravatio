# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_customimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
