# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-28 21:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0071_mergerequest_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvedchange',
            name='base_object_content_type',
        ),
        migrations.RemoveField(
            model_name='approvedchange',
            name='merge_request',
        ),
        migrations.RemoveField(
            model_name='approvedchange',
            name='updated_object_content_type',
        ),
        migrations.AlterModelOptions(
            name='mergerequest',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='mergerequest',
            name='closed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='closed by'),
        ),
        migrations.DeleteModel(
            name='ApprovedChange',
        ),
    ]