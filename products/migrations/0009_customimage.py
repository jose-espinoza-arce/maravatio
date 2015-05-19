# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_boxpresentation_bottlerow'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cimage', models.ImageField(default=b'/home/jose/dev/djangodev/maravatio/djmaravatio/static/generic_profile_image.png', upload_to=b'images/custom/')),
            ],
        ),
    ]
