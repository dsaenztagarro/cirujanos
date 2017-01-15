# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pathology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL Slug')),
                ('order', models.IntegerField(default=0)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name_plural': 'pathologies',
                'verbose_name': 'pathology',
            },
        ),
        migrations.CreateModel(
            name='PathologyArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Article')),
                ('pathology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Pathology')),
            ],
        ),
        migrations.CreateModel(
            name='PathologyVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(default='A', max_length=3)),
                ('pathology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Pathology')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL Slug')),
                ('order', models.IntegerField(default=0)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name_plural': 'procedures',
                'verbose_name': 'procedure',
            },
        ),
        migrations.CreateModel(
            name='ProcedureArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Article')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Procedure')),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(default='A', max_length=3)),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Procedure')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Video')),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='articles',
            field=models.ManyToManyField(through='web.ProcedureArticle', to='media.Article'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='videos',
            field=models.ManyToManyField(through='web.ProcedureVideo', to='media.Video'),
        ),
        migrations.AddField(
            model_name='pathology',
            name='articles',
            field=models.ManyToManyField(through='web.PathologyArticle', to='media.Article'),
        ),
        migrations.AddField(
            model_name='pathology',
            name='videos',
            field=models.ManyToManyField(through='web.PathologyVideo', to='media.Video'),
        ),
    ]
