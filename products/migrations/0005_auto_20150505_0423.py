# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150505_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='etype',
            field=models.ForeignKey(related_name='templates', default=1, to='products.EventType'),
        ),
    ]
