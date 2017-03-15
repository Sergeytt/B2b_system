# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zakupki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zakupki',
            options={'verbose_name': 'Закупки', 'verbose_name_plural': 'Закупки'},
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='code',
            field=models.CharField(max_length=40, verbose_name='Артикл'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='col',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='company',
            field=models.CharField(max_length=50, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='create_at',
            field=models.DateField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='manager',
            field=models.CharField(max_length=50, verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена закупки'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='price_sel',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена продажи'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='score',
            field=models.CharField(max_length=40, verbose_name='Счет'),
        ),
        migrations.AlterField(
            model_name='zakupki',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Статус'),
        ),
    ]
