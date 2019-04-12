# Generated by Django 2.1.7 on 2019-04-08 09:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20190323_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='college_id',
            field=models.CharField(editable=False, help_text='Enter the college roll number', max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Collge Id'),
        ),
        migrations.AlterField(
            model_name='student',
            name='join_year',
            field=models.DateField(default=datetime.datetime(2019, 4, 8, 9, 14, 38, 924366, tzinfo=utc), help_text='Select your date of join the college', verbose_name='DOJ'),
        ),
    ]