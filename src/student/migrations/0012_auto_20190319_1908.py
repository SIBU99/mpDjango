# Generated by Django 2.1.7 on 2019-03-19 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20190319_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='join_year',
            field=models.DateField(default=datetime.datetime(2019, 3, 19, 13, 38, 29, 767534, tzinfo=utc), help_text='Select your date of join the college', verbose_name='DOJ'),
        ),
    ]
