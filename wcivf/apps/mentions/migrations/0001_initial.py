# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elections', '0008_auto_20160405_1412'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(db_index=True, max_length=50)),
                ('date_order', models.DateTimeField()),
                ('date_published', models.DateTimeField(null=True)),
                ('quote', models.TextField(blank=True)),
                ('truncated_left', models.BooleanField(default=False)),
                ('truncated_right', models.BooleanField(default=False)),
                ('stream_item_id', models.CharField(db_index=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=500)),
                ('url', models.URLField(max_length=800)),
                ('people', models.ManyToManyField(to='people.Person')),
                ('posts', models.ManyToManyField(to='elections.Post')),
            ],
        ),
    ]
