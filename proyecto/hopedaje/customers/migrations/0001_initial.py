# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('client_premium', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('client', models.BooleanField(default=False)),
                ('date_premium', models.DateTimeField()),
                ('premiun_pay', models.CharField(max_length=14)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('phone', models.CharField(max_length=14, null=True, blank=True)),
                ('address', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('date_emision', models.DateField(null=True, blank=True)),
                ('city', models.CharField(max_length=20)),
                ('registration', models.CharField(max_length=1, null=True, blank=True)),
                ('name_registration', models.CharField(max_length=20, null=True, blank=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
