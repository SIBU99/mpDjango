from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import PaymentForm, FinalForm
from .models import Student, Document, Parent
from paytm.Checksum import generate_checksum
from json import dumps,loads
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from urllib.parse import urlencode

MERCHANT_KEY = "ocfB#cfv0he2A1i!"
class Helper():
    """
    This will deal with the student model easy work with view
    """
    def __init__(self,student):
        "this is the constructor for all the work related to the Helper"
        self.student = student
        self.course = self.courseDetector()
        self.branch =self.branchDetector()
        self.year = self.yearDetector()
        self.sem =self.semesterDetector()

    def courseDetector(self):
        "this will check selcted course and return the Course type"
        for i in self.student.cor:
            if self.student.course == "MCA" and i[0] == 'MCA':
                return i[1]
            else:
                for j in i[1]:
                    if self.student.course in j:
                        return i[0]
        
    def branchDetector(self):
        "this will check the branch detector"

        for i in self.student.cor:
            if self.student.course == 'MCA' and i[0] == 'MCA':
                    return i[1]
            else:
                    for j in i[1]:
                            if self.student.course in j:
                                    return j[1]

    def semesterDetector(self):
        "this return the semester"
        for i in self.student.sem:
            if self.student.semester in i:
                return i[1]

    def yearDetector(self):
        "this will return the year"
        for i in self.student.yr:
            if self.student.acc_year in i:
                return i[1]
 
# Create your views here.
def PrePaymnetSlipView(request):
    "this wil create the payment page"
    key = request.session.get('key')
    my_stud = Student.objects.get(reg_no = key )
    my_acc = 50000
    img = Document.objects.get(student = my_stud)
    h = Helper(my_stud)
    my_form  = PaymentForm()
    if request.method == "POST":
        my_form = PaymentForm(request.POST)
        if my_form.is_valid():
            holder = my_form.cleaned_data # this will hold the clean data
            for i in holder:
                if type(holder[i]) is not str:
                    holder[i] = str(holder[i])
            
            params = {
                "MID":holder['MID'],
                "ORDER_ID":holder['ORDER_ID'],
                "CUST_ID":holder['CUST_ID'],
                "TXN_AMOUNT":holder['TXN_AMOUNT'],
                "CHANNEL_ID":holder['CHANNEL_ID'],
                "INDUSTRY_TYPE_ID":holder['INDUSTRY_TYPE_ID'],
                "WEBSITE":holder['WEBSITE'],
            }
            #hold = generate_checksum(param_dict=params, merchant_key=MERCHANT_KEY, salt= None)
            params['CHECKSUMHASH'] = "checksum"
            params['REG_NO'] = my_stud.reg_no
            params['CALLBACK_URL'] = holder['CALLBACK_URL']
            params['EMAIL'] = holder['EMAIL']
            params['MOBILE_NO'] = holder["MOBILE_NO"]
            
            #pprint(params)
            
            holder  = dumps(params) #? this will hold the sting type of the json convert of params
            request.session['pass_data'] = holder #! this is a string in it. so we have to again process the srting to dic
            return redirect('pay2',) # this wil redirect the Pre Payment Reciept Page
        else:
            print(my_form._errors)
    context = {
        'form':my_form,
        'stud': my_stud,
        'acc':my_acc,
        'helper':h,
        'img':img
        }
    return render(request,'payment.htm',context)

#@csrf_exempt
def PrePaymentRecieptView(request):
    "this is the tes case of the PaymnetView"
    pprint(dict(request.session))

    holder =request.session.get('pass_data',None) # this will check weather the session data is not curropt
    if holder == None:
        return HttpResponseRedirect("<h1>Problem occured in session </h1>")
    else:
        holder = loads(holder) #loads the sting json as a dic of python
    
    #? this is the class for the holder
    class Holder:
        "this will hold all the value as a class for better use of the holder dictionary"
        pass
    #? class end here

    hold = Holder()
    hold.MID = holder.get('MID')
    hold.ORDER_ID = holder.get('ORDER_ID')
    hold.CUST_ID = holder.get('CUST_ID')
    hold.TXN_AMOUNT = holder.get('TXN_AMOUNT')
    hold.CHANNEL_ID = holder.get('CHANNEL_ID')
    hold.INDUSTRY_TYPE_ID = holder.get('INDUSTRY_TYPE_ID')
    hold.WEBSITE = holder.get('WEBSITE')
    hold.CHECKSUMHASH = holder.get('CHECKSUMHASH')

    #! Clearing the session for the better use
    #request.session.flush()
    #request.session.modified = True

    my_stud = Student.objects.get(reg_no = holder['REG_NO'])
    print(my_stud)
    my_acc = 50000
    img = Document.objects.get( student = my_stud )
    h = Helper(my_stud)
    my_form  = FinalForm()
    
    #if request.method == "POST":
    #    my_form = PaymentForm(request.POST)
    #    if my_form.is_valid():
    #        holder = my_form.cleaned_data # this will hold the clean data
    #        for i in holder:
    #            if type(holder[i]) is not str:
    #                holder[i] = str(holder[i])
    #    print("Ee"*20)
    #    pprint(holder)
        #encoded_args = urlencode(holder)
        #url = "https://securegw-stage.paytm.in/theia/processTransaction?" + encoded_args
        #print(url)
        #return HttpResponseRedirect()
    context = {
        'form':my_form,
        'img':img,
        'stud': my_stud,
        'acc':my_acc,
        'helper': h,
        'help': hold
        }
    return render(request,'payment2.htm',context)

@csrf_exempt
def TransactionView(request):
        "this will hold the values get from the response from the paytm api"
        if request.method == "POST":
            dic = {}
            for key in request.POST:
                dic[key] = request.POST[key]
            print(dic)
            context ={
                'text' : dic
            }
            return render(request,'respose.htm',context)

def StudHomeView(request):
    "this is for the student home page"
    key = request.session.get('key')
    s = Student.objects.get(reg_no = key)
    image = Document.objects.get(student = s)
    request.session['key'] = key
    context = {
        'stud':s,
        'img':image,
    }
    return render(request,'home_stud.htm', context)

def FeesView(request):
    "this will show all the fess detail of the student and will show how much he have to pay and and payment history"
    key = request.session.get('key')
    stud = Student.objects.get(reg_no = key)
    img  = Document.objects.get( student = stud )
    context={
        'stud':stud,
        'img':img
    }
    return render(request,'stud_home/fees.htm',context)

def WhoamiView(request):
    "this will render the 'who am i' page ...  :)"
    key = request.session.get('key')
    stud = Student.objects.get(reg_no = key)
    h = Helper(stud)
    parent = Parent.objects.get(student = stud )
    img = Document.objects.get(student = stud )
    context = {
        'stud':stud,
        'img':img,
        'helper':h,
        'par': parent,
    }
    return render(request,'stud_home/whoami.htm',context)