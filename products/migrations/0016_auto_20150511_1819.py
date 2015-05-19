# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150511_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxpresentation',
            old_name='bimage',
            new_name='img_original_size',
        ),
        migrations.AddField(
            model_name='boxpresentation',
            name='img_tag',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/boxpresentation/'),
        ),
        migrations.AddField(
            model_name='boxpresentation',
            name='img_zoom_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/boxpresentation/'),
        ),
    ]
