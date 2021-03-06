# Generated by Django 2.1.7 on 2019-03-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190315_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odr', models.CharField(help_text='If the order is created and procced to pay then only it will store the order id', max_length=50, unique=True, verbose_name='Order Id')),
            ],
        ),
    ]
