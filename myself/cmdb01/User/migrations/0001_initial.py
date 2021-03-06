# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmdbUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('phone', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('photo', models.ImageField(upload_to=b'image', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe7\xa7\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.TextField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('obj_id', models.IntegerField(verbose_name=b'\xe8\xa2\xab\xe6\x93\x8d\xe4\xbd\x9c\xe5\xaf\xb9\xe8\xb1\xa1')),
            ],
        ),
        migrations.CreateModel(
            name='Permission_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission_id', models.IntegerField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90id')),
                ('group_id', models.IntegerField(verbose_name=b'\xe7\xbb\x84id')),
            ],
        ),
        migrations.CreateModel(
            name='User_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8did')),
                ('group_id', models.IntegerField(verbose_name=b'\xe7\xbb\x84id')),
            ],
        ),
        migrations.CreateModel(
            name='User_permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8did')),
                ('permission_id', models.IntegerField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90id')),
            ],
        ),
    ]
