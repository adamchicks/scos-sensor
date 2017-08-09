# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 17:16
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import schedule.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleEntry',
            fields=[
                ('name', models.SlugField(primary_key=True, serialize=False)),
                ('action', models.CharField(choices=[(b'logger', b'logger - Log the message "running test {name}/{tid}" at log level INFO.'), (b'mock_acquire', b'mock_acquire - Test an acquisition without using the radio.')], max_length=50)),
                ('priority', models.SmallIntegerField(default=10)),
                ('start', models.BigIntegerField(blank=True, default=schedule.models.next_schedulable_timefn)),
                ('stop', models.BigIntegerField(blank=True, null=True)),
                ('relative_stop', models.BooleanField(default=False)),
                ('interval', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('active', models.BooleanField(default=True)),
                ('next_task_time', models.BigIntegerField(editable=False, null=True)),
                ('next_task_id', models.IntegerField(default=1, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'db_table': 'schedule',
            },
        ),
    ]
