from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from student.validators import validate_registor_no
#password validation and the registarion number
def passwordVaild(value):
    "this will check the creteria for the password content"
    charList = ['!','@','#','?']
    smallAlphabet = [ chr(i) for i in range(ord('a'),ord('z')+1)]
    capAlphabet = [ chr(i) for i in range(ord('A'),ord('Z')+1)]
    charPass,smallPass,capPass = False,False,False

    for alpha in value:
    #this will check the atleast one character for the is present of charList
        if alpha in charList:
            charPass =True
    #this will check atleast one character present in smallAlphabet
        elif alpha in smallAlphabet:
            smallPass = True
    #this will check atleast one character present in capAlphabet 
        elif alpha in capAlphabet:
            capPass = True
    
     #this will check the length of the vlaue 
    if charPass and smallPass and capPass:
        if len(value) >= 6:
            return value
        else:
            raise ValidationError(_('Password must have the Atleast 6 character'))
    else:
        raise ValidationError(_('Password Must have atleast one capital letter, one small letter and one special character from !, @, #, ?'))

def idValid(value):
    "this will check the valid user id"
    if "@cvrce.com" in str(value):
        return value
    else:
        raise ValidationError(_("Invalid User ID ]::[ So enter wisely"))
# Create your models here.
class Login(models.Model):
    "this will store the list of all the user_login the system"

    id_user = models.CharField(
        verbose_name="UserID",
        max_length = 30,
        help_text = "Enter the college unquie login assigned",
        unique = True,
        primary_key = True,
        validators = [ idValid ]
    )
    pass_word = models.CharField(
        verbose_name="Password",
        max_length =50,
        help_text = "Enter the your password",
        validators = [ passwordVaild, ]
    )
    key = models.BigIntegerField(
        verbose_name = "Access ID",
        help_text= "This May be Student ID or Teacher ID or any numeric access number",
        unique=True,
    )
    u_type = models.CharField(
        verbose_name = "User Type",
        help_text = "This is the type of user using it",
        max_length = 20,
        choices= [
            ('stud','Student'),
            ('ment','Mentor'),
            ('exam','Examinations'),
            ('acc','Accounts')
        ]
    ) 

    def __str__(self):
        return f'{self.id_user}'