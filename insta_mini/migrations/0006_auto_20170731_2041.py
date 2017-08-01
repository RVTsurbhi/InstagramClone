# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta_mini', '0005_auto_20170731_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to=b'user_images')),
                ('image_url', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta_mini.UserModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sessiontoken',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
