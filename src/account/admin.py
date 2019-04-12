from django.contrib import admin
from .models import TransactionHolder,CardHolder,Order
# Register your models here.
admin.site.register(TransactionHolder)
admin.site.register(CardHolder)
admin.site.register(Order)