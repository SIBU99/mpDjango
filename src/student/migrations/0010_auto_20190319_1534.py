# Generated by Django 2.1.7 on 2019-03-19 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20190319_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='join_year',
            field=models.DateField(default=datetime.datetime(2019, 3, 19, 10, 4, 23, 392451, tzinfo=utc), help_text='Select your date of join the college', verbose_name='DOJ'),
        ),
    ]