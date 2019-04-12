from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def TestView(request):
    "this is the test of the GET"
    context = {}
    return render(request,'testing.htm',context)