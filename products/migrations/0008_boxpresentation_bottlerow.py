# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_tequilatype_maskimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxpresentation',
            name='bottlerow',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
    ]
