# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-09 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0110_initialapplicationreview_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantapproval',
            name='review_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationReviewer'),
        ),
    ]
