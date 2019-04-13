from django.shortcuts import render
from .models import Mentor as M
from student.models import Student as S
from student.views import Helper
# Create your views here.
def DashView(request):
    "this will hold the view for the student dash board"
    key = request.session.get('key')
    ment = M.objects.get(id_fet = key)
    stud_list = list(S.objects.filter( ment = ment ))
    helper = list(map(Helper,stud_list))
    zipper = zip(stud_list,helper)
    context={
        'ment':ment,
        'zip' : zipper,
    }
    return render(request,'student_dash.htm',context)

def MentHomeView(request):
    "this is the view for the mentors main view"
    key  = request.session.get('key')
    print(f"acess key is ]:[ {key}")
    m = M.objects.get(id_fet = key)
    context = {
        'ment':m,
    }
    return render(request,'menthome.htm',context)

def whoIam(request):
    "this is for the detail information for the mentor"
    key = request.session.get('key')
    ment = M.objects.get(id_fet = key)
    context = {
        'ment':ment
    }
    return render(request,'navMentor/profiledata.htm',context)