# Generated by Django 2.1.7 on 2019-03-19 10:04

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.CharField(help_text='Enter the college unquie login assigned', max_length=30, primary_key=True, serialize=False, unique=True, validators=[login.models.idValid], verbose_name='UserID')),
                ('pass_word', models.CharField(help_text='Enter the your password', max_length=50, validators=[login.models.passwordVaild], verbose_name='Password')),
                ('key', models.BigIntegerField(help_text='This May be Student ID or Teacher ID or any numeric access number', unique=True, verbose_name='Access ID')),
                ('u_type', models.CharField(help_text='This is the type of user using it', max_length=20, verbose_name='User Type')),
            ],
        ),
    ]
