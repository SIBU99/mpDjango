# Generated by Django 2.1.7 on 2019-03-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardHolder',
            fields=[
                ('txn_id', models.CharField(help_text='It stores the Unique Transaction ID of Paytm', max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='Transaction IP(Paytm)')),
                ('pay_id', models.CharField(help_text='This will store the unique paymnet id for the student', max_length=30, verbose_name='Students Paymnet Id')),
                ('bin_number', models.CharField(help_text='This will Store the First 6 Digits of Credit/Debit Card', max_length=6, verbose_name='Starting Digits')),
                ('card_last_nums', models.CharField(help_text='This will Store the last 4 Digits of Credit/Debit Card', max_length=4, verbose_name='Ending Digits')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionHolder',
            fields=[
                ('txn_id', models.CharField(help_text='It stores the Unique Transaction ID of Paytm', max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='Transaction IP(Paytm)')),
                ('pay_id', models.CharField(help_text='This will store the unique paymnet id for the student', max_length=30, verbose_name='Students Paymnet Id')),
                ('banktxn_id', models.TextField(blank=True, help_text='This will store the Unique Transaction Id by bank', null=True, verbose_name='Bank Transaction Id')),
                ('order_id', models.CharField(help_text='This will Store the order_id', max_length=50, verbose_name='Order ID')),
                ('txt_amount', models.CharField(help_text='This will store the Amount Paid', max_length=10, verbose_name='Amount Paid')),
                ('currency', models.CharField(default='INR', help_text='This will store the Type Of Currency', max_length=3, verbose_name='Currency')),
                ('status', models.CharField(help_text='This will store the status of the paytm', max_length=20, verbose_name='Paytm Status')),
                ('txt_date', models.DateTimeField(help_text='This will store the Date And Time Of Transaction', verbose_name='Transaction Date And Time')),
                ('gatewayname', models.CharField(blank=True, help_text='This will store the Gateway', max_length=15, verbose_name='Gateway Field')),
                ('bank_name', models.CharField(blank=True, help_text='This will store the Bank Name', max_length=500, verbose_name='Bank Name')),
                ('payment_mode', models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card'), ('NB', 'Net Banking'), ('UPI', 'UPI'), ('PPI', 'Paytm Wallet')], default='CC', help_text='This will store the Payment Mode', max_length=15, verbose_name='Payment Mode')),
                ('card', models.CharField(choices=[('T', 'Truth'), ('F', 'False')], default='False', help_text='This will store the use of card', max_length=5, verbose_name='Card In Use')),
            ],
        ),
    ]
