# Generated by Django 2.1.7 on 2019-03-19 10:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190318_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='acc_year',
            field=models.CharField(choices=[('first', 'First Year'), ('second', 'Second Year'), ('third', 'Third Year'), ('fourth', 'Fourth Year')], default='First Year', help_text='Select your Accademic Year', max_length=6, verbose_name='Accademic Year'),
        ),
        migrations.AlterField(
            model_name='student',
            name='join_year',
            field=models.DateField(default=datetime.datetime(2019, 3, 19, 10, 1, 19, 793496, tzinfo=utc), help_text='Select your date of join the college', verbose_name='DOJ'),
        ),
    ]
