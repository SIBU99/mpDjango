from django.db import models

# Create your models here.
class Mentor(models.Model):
    "this will store the data of the mentor and related data and allow the mentor to add the documents of the student"
    p =[
        ('ASS_P','Ass. Professor'),
        ('ASO_P','Aso. Professor'),
        ('PROF','Professor'),
        ('HOD','Head Of Department')
    ]
    emp_id = models.CharField(
        verbose_name = "Teacher ID",
        help_text = "Enter the Mentor's Teacher's ID",
        max_length = 10,
        unique = True,
        primary_key = True
    )
    name = models.CharField(
        verbose_name = "Mentor's Name",
        help_text = "Name of your Mentor",
        max_length = 40
    )
    contact = models.BigIntegerField(
        verbose_name= "Contact Number",
        help_text= "Enter the Mentor's Contact No",
        blank= False,
        unique= True,
    )
    dept = models.CharField(
        verbose_name = "Department",
        help_text = "Enter the Mentor's Department",
        max_length = 50
    )
    pos = models.CharField(
        verbose_name = "Post",
        help_text = "Enter the Mentor's Post",
        max_length= 40,
        choices = p
    )

    def __str__(self):
        "To String for the model which return the name"
        return f'{self.name}'
    