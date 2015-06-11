# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAuditLogEntry',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', auto_created=True, blank=True)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], editable=False)),
                ('action_user', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, editable=False, related_name='_comment_audit_log_entry', null=True)),
                ('post', models.ForeignKey(to='blog.Post', related_name='_auditlog_comments')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
    ]
