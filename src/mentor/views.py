from django.shortcuts import render, HttpResponse
from .models import Mentor as M
from student.models import Student as S
from student.models import Document as dc
from student.models import Parent
from student.views import Helper
# Create your views here.
def DashView(request):
    "this will hold the view for the student dash board"
    key = request.session.get('key')
    ment = M.objects.get(id_fet = key)
    stud_list = list(S.objects.filter( ment = ment ))
    helper = list(map(Helper,stud_list))
    Doc_list = [] # this will store the data of all the student related to document
    for i in stud_list:
        Doc_list += [dc.objects.get(student = i) ]
    zipper = zip(stud_list,helper,Doc_list)
    
    if request.method == "POST":
        print(request.POST)

    context={
        'ment':ment,
        'zip' : zipper,
        'students':stud_list,
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

def displayStudent(request, RegNo):
    "this is used for the registration navigation of site"
    key = request.session.get('key')
    ment = M.objects.get(id_fet = key)
    RegNo = int(RegNo)
    stud = S.objects.get(reg_no = RegNo)
    h = Helper(stud)
    parent = Parent.objects.get(student = stud )
    img = dc.objects.get(student = stud )
    context = {
        'ment':ment,
        'stud':stud,
        'img':img,
        'helper':h,
        'par': parent,
    }
    return render(request,'datadisplayer.htm',context)