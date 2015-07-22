# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='materia_prima',
            field=models.ForeignKey(to='recetas.MateriaPrima'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receta',
            field=models.ForeignKey(to='recetas.Receta'),
        ),
    ]
