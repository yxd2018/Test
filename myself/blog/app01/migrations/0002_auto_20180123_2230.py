# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenic1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=64, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('time', models.DateField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('img', models.ImageField(upload_to=b'pic', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87')),
            ],
        ),
        migrations.CreateModel(
            name='Scenic2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=64, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('time', models.DateField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('img', models.ImageField(upload_to=b'pic', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87')),
            ],
        ),
        migrations.CreateModel(
            name='Scenic3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=64, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('time', models.DateField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('img', models.ImageField(upload_to=b'pic', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87')),
            ],
        ),
        migrations.AlterField(
            model_name='home1',
            name='img',
            field=models.ImageField(upload_to=b'pic', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87'),
        ),
    ]
