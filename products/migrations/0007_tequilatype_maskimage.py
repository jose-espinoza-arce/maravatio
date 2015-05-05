# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150505_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='tequilatype',
            name='maskimage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/tequila/'),
        ),
    ]
