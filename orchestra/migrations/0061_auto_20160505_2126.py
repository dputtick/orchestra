# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import orchestra.models.communication.mixins
import orchestra.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0060_auto_20160505_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffBotRequest',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('required_role_counter', models.IntegerField()),
                ('request_cause', models.IntegerField(choices=[
                 (0, 'user'), (1, 'autostaff'), (2, 'restaff')])),
                ('project_description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[
                 (0, 'processing'), (1, 'complete')], default=0)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='staffing_requests', to='orchestra.Task')),
            ],
            options={
                'abstract': False,
            },
            bases=(orchestra.models.communication.mixins.StaffBotRequestMixin,
                   orchestra.utils.models.DeleteMixin, models.Model),
        ),
        migrations.RemoveField(  # manually-reviewed
            model_name='staffingrequestinquiry',
            name='project_description',
        ),
        migrations.RemoveField(  # manually-reviewed
            model_name='staffingrequestinquiry',
            name='request_cause',
        ),
        migrations.RemoveField(  # manually-reviewed
            model_name='staffingrequestinquiry',
            name='required_role',
        ),
        migrations.RemoveField(  # manually-reviewed
            model_name='staffingrequestinquiry',
            name='status',
        ),
        migrations.RemoveField(  # manually-reviewed
            model_name='staffingrequestinquiry',
            name='task',
        ),
        migrations.AlterField(  # manually-reviewed
            model_name='staffingresponse',
            name='request',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='orchestra.StaffingRequestInquiry'),
        ),
        migrations.AddField(
            model_name='staffingrequestinquiry',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='inquiries', to='orchestra.StaffBotRequest'),
        ),
    ]
