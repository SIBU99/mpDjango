from django.db import models

# Create your models here.
def upload_to(instance, filename):
    "this will upload the file in the dp/<mentor.emp_id>/filename"
    return f'dp/{instance.emp_id}/filename'
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
    id_fet = models.IntegerField(
        verbose_name="Unique ID",
        help_text="unique ID wrt College",
        blank=True
    )
    dp = models.ImageField(
        verbose_name="Profile Picture",
        help_text="This is the Profile Pictuer of the Mentor",
        upload_to = upload_to,
        default = 'dp/default/default.png'
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
    