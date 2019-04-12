from django.shortcuts import render,redirect
from .forms import LoginForm
from .models import Login
# Create your views here.
def login_view(request):
    "this will render the login page for the user of this site"
    my_form = LoginForm()
    
    context = {'form':my_form}
    return render(request,'login/login.htm', context)

def home_view(request):
    "this will render the home page for the user"
    my_form = LoginForm()
    if request.method == 'POST':
        data =  LoginForm(request.POST)
        print('it is in first layer') #added comment
        if data.is_valid():
            username = data.cleaned_data['id_user']
            passwd = data.cleaned_data['pass_user']
            print(f'username = {username} passwaord = {passwd}')
            try:
                l = Login.objects.get( id_user = username )
                print(f"The instance {l}")
                if l.pass_word == passwd:
                    request.session['key'] = l.key
                    if l.u_type == 'stud':
                        return redirect('stud_home') # this is for the stuedent
                    elif l.u_type == 'ment':
                        return redirect() # this is for the mentor
                    elif l.u_type == 'exam':
                        return redirect() # this is for the examination cell
                    elif l.u_type == 'acc':
                        return redirect() # this is for the accounts
                else:
                    raise AttributeError
            except:
                print('objects not found')
                pass
    context = {
        'check':True,
        'range':range(15),
        'form':my_form
    }
    return render(request,'login/home.htm',context)