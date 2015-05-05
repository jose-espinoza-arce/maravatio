# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150505_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='tequilatype',
            name='bimage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/tequila/'),
        ),
        migrations.AlterField(
            model_name='template',
            name='timage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/templates/'),
        ),
    ]
