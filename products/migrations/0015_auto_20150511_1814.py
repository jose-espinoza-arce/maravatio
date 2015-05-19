# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_boxpresentation_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxpresentation',
            old_name='timage',
            new_name='bimage',
        ),
        migrations.AlterField(
            model_name='boxpresentation',
            name='type',
            field=models.ForeignKey(related_name='sizes', default=1, to='products.TequilaType'),
        ),
    ]
