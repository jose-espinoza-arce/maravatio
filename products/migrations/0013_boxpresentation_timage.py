# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20150509_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxpresentation',
            name='timage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/boxpresentation/'),
        ),
    ]
