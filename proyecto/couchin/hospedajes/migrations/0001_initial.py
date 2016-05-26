# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('pregunta', models.TextField()),
                ('respuesta', models.TextField()),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'hospedaje')),
            ],
        ),
        migrations.CreateModel(
            name='Hospedaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('localidad', models.CharField(max_length=250)),
                ('ciudad', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('capacidad', models.IntegerField()),
                ('descripcion', models.TextField(max_length=250)),
                ('titulo', models.CharField(max_length=250)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoHospedaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='hospedaje',
            name='tipo',
            field=models.ForeignKey(to='hospedajes.TipoHospedaje'),
        ),
        migrations.AddField(
            model_name='foto',
            name='hospedaje',
            field=models.ForeignKey(to='hospedajes.Hospedaje'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='hospedaje',
            field=models.ForeignKey(to='hospedajes.Hospedaje'),
        ),
    ]
