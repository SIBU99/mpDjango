from django.contrib import admin
from .models import Student,Parent,Document
# Register your models here.
admin.site.register(Document)
admin.site.register(Student)
admin.site.register(Parent)