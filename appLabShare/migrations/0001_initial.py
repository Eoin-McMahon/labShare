# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 15:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('level', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labNumber', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appLabShare.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('attachedFile', models.FileField(blank=True, default='', null=True, upload_to='lab_files')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Student', max_length=7)),
                ('name', models.CharField(default='', max_length=128)),
                ('picture', models.ImageField(default='profile_images/user_image.png', upload_to='profile_images')),
                ('bio', models.CharField(default='', max_length=128)),
                ('degree', models.CharField(default='', max_length=128)),
                ('university', models.CharField(default='', max_length=128)),
                ('facebook', models.URLField(default='', max_length=300)),
                ('instagram', models.URLField(default='', max_length=300)),
                ('twitter', models.URLField(default='', max_length=300)),
                ('linkedIn', models.URLField(default='', max_length=300)),
                ('github', models.URLField(default='', max_length=300)),
                ('courses', models.ManyToManyField(to='appLabShare.Course')),
                ('friends', models.ManyToManyField(to='appLabShare.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appLabShare.UserProfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='postedIn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appLabShare.Lab'),
        ),
        migrations.AddField(
            model_name='lab',
            name='peopleInLab',
            field=models.ManyToManyField(to='appLabShare.UserProfile'),
        ),
    ]
