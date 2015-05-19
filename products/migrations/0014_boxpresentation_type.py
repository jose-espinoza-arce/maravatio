# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_boxpresentation_timage'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxpresentation',
            name='type',
            field=models.ForeignKey(related_name='presentations', default=1, to='products.TequilaType'),
        ),
    ]
