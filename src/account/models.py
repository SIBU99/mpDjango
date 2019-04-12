from django.db import models
from student.models import Student

# Create your models here. 
class TransactionHolder(models.Model):
    "this will hold the set of response from paytm api for better solving the transaction details"
    ch = [
        ('CC','Credit Card'),
        ('DC','Debit Card'),
        ('NB','Net Banking'),
        ('UPI','UPI'),
        ('PPI','Paytm Wallet')
    ]
    
    txn_id = models.CharField(
        verbose_name = "Transaction IP(Paytm)",
        help_text = "It stores the Unique Transaction ID of Paytm",
        max_length= 64,
        primary_key = True,
        unique = True
    )
    pay_id= models.CharField(
        verbose_name = "Students Paymnet Id",
        help_text = "This will store the unique paymnet id for the student",
        max_length = 30,
        #? <passing_yr>@<reg_no><college_id>$<birth_year>_<birth_month>_<birth_date>!
    )
    banktxn_id = models.TextField(
        verbose_name = "Bank Transaction Id",
        help_text = "This will store the Unique Transaction Id by bank",
        blank = True,
        null = True  
    )
    order_id = models.CharField(
        verbose_name="Order ID",
        help_text = "This will Store the order_id",
        max_length = 50
    )
    txt_amount = models.CharField(
        verbose_name = "Amount Paid",
        help_text = "This will store the Amount Paid",
        max_length = 10,
    )
    currency = models.CharField(
        verbose_name = "Currency",
        help_text = "This will store the Type Of Currency",
        max_length = 3,
        default = "INR"
    )
    status = models.CharField(
        verbose_name = "Paytm Status",
        help_text = "This will store the status of the paytm",
        max_length = 20
    )
    txt_date = models.DateTimeField( #yyyy-mm-dd hh:mm:ss
        verbose_name="Transaction Date And Time",
        help_text= "This will store the Date And Time Of Transaction"
    )
    gatewayname = models.CharField(
        verbose_name = "Gateway Field",
        help_text = "This will store the Gateway",
        max_length = 15,
        blank = True, 
    )
    bank_name = models.CharField(
        verbose_name = "Bank Name",
        help_text = "This will store the Bank Name",
        max_length = 500,
        blank = True
    )
    payment_mode = models.CharField(
        verbose_name = "Payment Mode",
        help_text = "This will store the Payment Mode",
        max_length = 15,
        choices = ch,
        default = "CC"
    )
    card =models.CharField(
        verbose_name = "Card In Use",
        help_text = "This will store the use of card",
        max_length = 5,
        choices = [
            ('T','True'),
            ('F',"False")
        ],
        default = "False"
    )

    def __str__(self):
        "to string function"
        return f'{self.txn_id}'

class CardHolder(models.Model):
    "this will hold the card transaction set"
    txn_id = models.CharField(
        verbose_name = "Transaction IP(Paytm)",
        help_text = "It stores the Unique Transaction ID of Paytm",
        max_length= 64,
        primary_key = True,
        unique = True
    )
    pay_id= models.CharField(
        verbose_name = "Students Paymnet Id",
        help_text = "This will store the unique paymnet id for the student",
        max_length = 30,
        #? <passing_yr>@<reg_no><college_id>$<birth_year>_<birth_month>_<birth_date>!
    )
    bin_number = models.CharField(
        verbose_name = "Starting Digits",
        help_text = "This will Store the First 6 Digits of Credit/Debit Card",
        max_length  = 6,
    )
    card_last_nums = models.CharField(
        verbose_name = "Ending Digits",
        help_text = "This will Store the last 4 Digits of Credit/Debit Card",
        max_length = 4
    )

class Order(models.Model):
    "this will deal with the order id of the each tracsaction and create a new trasaction id"

    odr = models.CharField(
        verbose_name = "Order Id",
        help_text ="If the order is created and procced to pay then only it will store the order id  <year>_<month>@<day>_<sl_no>",
        unique = True,
        max_length = 50
    )

    def __str__(self):
        return f'{self.odr}'
