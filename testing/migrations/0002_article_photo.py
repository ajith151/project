# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2015, 10, 5, 10, 12, 53, 133000, tzinfo=utc), upload_to=b'images/'),
            preserve_default=False,
        ),
    ]
