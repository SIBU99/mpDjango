# Generated by Django 2.1.7 on 2019-04-12 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20190412_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='join_year',
            field=models.DateField(default=datetime.datetime(2019, 4, 12, 15, 41, 10, 247666, tzinfo=utc), help_text='Select your date of join the college', verbose_name='DOJ'),
        ),
    ]
