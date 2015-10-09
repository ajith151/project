# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_auto_20151005_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
