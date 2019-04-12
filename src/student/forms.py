from django import forms
from .models import Student

def createOrderId():
    "this will create a order id and send it to the from"
    try:
        from account.models import Order
        from datetime import datetime as dt
    except ImportError as ie:
        print(ie)
    
    data1, data2, data3 = dt.now().year, dt.now().month, dt.now().day
    num = Order.objects.count()
    if num == None:
        return f'{data1}_{data2}@{data3}_1'
    else:
        return f'{data1}_{data2}@{data3}_{num+1}'



#! createing the forms for the student app
class PaymentForm(forms.Form):
    "this will send requset to Paytm api and recives the response"

    MID = forms.CharField(
        max_length= 20,
        help_text = "It will store the the merchant id",
        widget = forms.HiddenInput(
            attrs={
                'value': 'ogYlZP62946399077470' #todo Use the merchant id
            }
        )
    )

    WEBSITE = forms.CharField(
        max_length=30,
        help_text ="this will use for stagging",
        widget = forms.HiddenInput(
            attrs={
                'value':"WEBSTAGING"
            }
        )
    )

    ORDER_ID = forms.CharField(
        max_length=50,
        help_text = "This will store the unique order id",
        widget = forms.HiddenInput(
            attrs={
                'value':f"{createOrderId()}" #make a function for generating the paytm oder id
            }
        )
    )
    CUST_ID = forms.CharField(
        max_length=64,
        help_text = "This will hold yhe unique pay id ",
        widget =  forms.HiddenInput(
            attrs={
                'value' : 'pay_id', # write a function to get the pay id
            }
        )
    )
    MOBILE_NO =forms.IntegerField(
        help_text = "This will store the phone number of the user",
        widget = forms.HiddenInput(
            attrs={
                'value':'phone number' #to fetch the phone number of the user
            }
        )
    )
    EMAIL = forms.EmailField(
        help_text =  "This will store the email of the user",
        widget = forms.HiddenInput(
            attrs={
                'value':'email' #write the function to fetch the email of the user
            }
        )
    )
    INDUSTRY_TYPE_ID = forms.CharField( 
        max_length=20,
        help_text = "This will  store the industy type passed by the user",
        widget = forms.HiddenInput(
            attrs={
                'value':'Retail' #tcheck the industry type from the paytm site
            }
        )
    )
    CHANNEL_ID =forms.CharField(
         max_length=10,
         help_text = "This will store the channel id passed by the user",
         widget = forms.HiddenInput(
             attrs={
                 'value':'WEB'
             }
         )
    )
    TXN_AMOUNT = forms.DecimalField(
        label = "Amount",
        min_value=5000,
        help_text = "This will hold the amount to be paid",
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'5000+'
            }
        )
    )
    CALLBACK_URL = forms.URLField(
        help_text = "this will hold the merchant response website",
        widget = forms.HiddenInput(
            attrs={
                'value':'http://127.0.0.1:8000/payment/' 
            }
        )
    )
    """
    CHECKSUMHASH = forms.CharField(
        max_length=180,
        help_text = "This will hold the automatic generated checksumhash string",
        widget = forms.HiddenInput(
            attrs={ 
                'value':'' #call the function and store the checksumhash 
            }
        )
    )
    """

class FinalForm(forms.Form):
    "this is the hidden form fileds filled for the final checkout of the payment page"
    MID = forms.CharField(
        max_length= 20,
        help_text = "It will store the the merchant id",
        widget = forms.HiddenInput(
            attrs={
                'value': 'ogYlZP62946399077470' #todo Use the merchant id
            }
        )
    )

    WEBSITE = forms.CharField(
        max_length=30,
        help_text ="this will use for stagging",
        widget = forms.HiddenInput(
            attrs={
                'value':"WEBSTAGING"
            }
        )
    )

    ORDER_ID = forms.CharField(
        max_length=50,
        help_text = "This will store the unique order id",
        widget = forms.HiddenInput(
            attrs={
                'value':f"{createOrderId()}" #make a function for generating the paytm oder id
            }
        )
    )
    CUST_ID = forms.CharField(
        max_length=64,
        help_text = "This will hold yhe unique pay id ",
        widget =  forms.HiddenInput(
            attrs={
                'value' : 'pay_id', # write a function to get the pay id
            }
        )
    )
    MOBILE_NO =forms.IntegerField(
        help_text = "This will store the phone number of the user",
        widget = forms.HiddenInput(
            attrs={
                'value':'phone number' #to fetch the phone number of the user
            }
        )
    )
    EMAIL = forms.EmailField(
        help_text =  "This will store the email of the user",
        widget = forms.HiddenInput(
            attrs={
                'value':'email' #write the function to fetch the email of the user
            }
        )
    )
    INDUSTRY_TYPE_ID = forms.CharField( 
        max_length=20,
        help_text = "This will  store the industy type passed by the user",
        widget = forms.HiddenInput(
            attrs={
                'value':'Retail' #tcheck the industry type from the paytm site
            }
        )
    )
    CHANNEL_ID =forms.CharField(
         max_length=10,
         help_text = "This will store the channel id passed by the user",
         widget = forms.HiddenInput(
             attrs={
                 'value':'WEB'
             }
         )
    )
    TXN_AMOUNT = forms.CharField(
        help_text = "This will hold the amount to be paid",
        widget = forms.HiddenInput(
            attrs={
                "value":'TXN_AMOUNT'
                }
        )
    )
    CALLBACK_URL = forms.URLField(
        help_text = "this will hold the merchant response website",
        widget = forms.HiddenInput(
            attrs={
                'value':'http://127.0.0.1:8000/response/' 
            }
        )
    )
    
    CHECKSUMHASH = forms.CharField(
        max_length=180,
        help_text = "This will hold the automatic generated checksumhash string",
        widget = forms.HiddenInput(
            attrs={
                "value":'checksumhash' 
            }
        )
    )
    
