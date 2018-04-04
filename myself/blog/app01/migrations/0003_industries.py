# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180123_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=64, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('time', models.DateField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
    ]
