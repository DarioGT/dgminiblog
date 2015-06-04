# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('status', models.CharField(null=True, max_length=20, blank=True)),
                ('info', jsonfield2.fields.JSONField(default={})),
            ],
        ),
    ]
