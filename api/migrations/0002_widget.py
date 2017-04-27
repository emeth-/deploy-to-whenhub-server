# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referrer_url', models.TextField(null=True, blank=True)),
                ('whenhub_url', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Widget',
                'verbose_name_plural': 'Widgets',
            },
        ),
    ]
