# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_article_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='photo',
            new_name='hero_image',
        ),
        migrations.AddField(
            model_name='article',
            name='auther',
            field=models.CharField(default=datetime.datetime(2015, 10, 5, 12, 5, 19, 360000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=datetime.datetime(2015, 10, 5, 12, 5, 30, 842000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default=datetime.datetime(2015, 10, 5, 12, 5, 43, 543000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 12, 5, 51, 189000, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
