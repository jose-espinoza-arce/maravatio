# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_boxpresentation'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='etype',
            field=models.ForeignKey(default=1, to='products.EventType'),
        ),
        migrations.AddField(
            model_name='template',
            name='timage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/static/generic_profile_image.png', upload_to=b''),
        ),
    ]
