# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-03 22:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TBLSessions', '0013_auto_20180203_2043'),
        ('groups', '0004_remove_group__is_closed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irat', models.FloatField(default=0.0, help_text='iRAT test grade.', verbose_name='iRAT grade')),
                ('grat', models.FloatField(default=0.0, help_text='gRAT test grade.', verbose_name='gRAT grade')),
                ('practical', models.FloatField(default=0.0, help_text='Practical test grade.', verbose_name='Practical test grade')),
                ('peer_review', models.FloatField(default=0.0, help_text='Peer review grade.', verbose_name='Peer review grade')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date that the session is created.', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date that the session is updated.', verbose_name='Updated at')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='groups.Group', verbose_name='Group')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='TBLSessions.TBLSession', verbose_name='TBL Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['session', 'user', 'created_at'],
                'verbose_name_plural': 'TBL Sessions grades',
                'verbose_name': 'TBL Session grades',
            },
        ),
    ]