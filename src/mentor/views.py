from django.shortcuts import render
from .models import Mentor as M
from student.models import Student as S
# Create your views here.
def DashView(request):
    "this will hold the view for the student dash board"
    #m = M.objects.get(emp_id = "#pass a emp_id")
    #stud_hold = S.objects.filter(ment = "#pass a mentor in_charge")
    context = {}
    return render(request,'student_dash.htm',context)