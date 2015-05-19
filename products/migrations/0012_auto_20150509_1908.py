# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150509_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customimage',
            old_name='cimage',
            new_name='file',
        ),
    ]
