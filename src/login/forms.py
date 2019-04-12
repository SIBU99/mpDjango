from django import forms

#createing the forms
class LoginForm(forms.Form):
    "this will check the user login in Login model"

    id_user = forms.CharField(
        label = "User Id",
        max_length=30,
        min_length=10,
        widget = forms.TextInput(
            attrs={
                'type':'text',
                'class':'form-control',
                'id' : 'inputId',
                'placeholder' : 'Unique User ID',

            }
        )
    )

    pass_user = forms.CharField(
        label = "Password",
        max_length=50,
        min_length=6,
        widget = forms.PasswordInput(
            attrs={
                'type':'password',
                'class':'form-control',
                'id':'inputPassword',
                'placeholder':'Password',
            }
        )
    )