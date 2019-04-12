from django.db import models
from mentor.models import Mentor
from .validators import validate_registor_no,validate_register_content
from django.utils import timezone as tz 
import os #python module is imported
from mpDjango.settings import BASE_DIR
from shutil import move #python module is imported
#BASE_DIR ]X[ c:\Users\kumar\Documents\mpDjango\src

# Create your models here.
def upload_to(instance, filename):
    "this will upload the file to the desire file location"
    return f"Docstore/{instance.student.reg_no}/{filename}"

class Student(models.Model):
    "this is the entity handeling with the student data in sqlite DB"
    #this is the choice list
    cor = [ #? This is the choice for the courses
        ('B.tech',(
            ('CSE','Computer Science Engineering'),
            ('ETC','Electronic Telecommunication Engineering'),
            ('EE','Electrical Engineering'),
            ('CE','Chemical Engineering'),
            ('ME','Mechanical Engineering'),
            ('CVE','Civil Engineering'),
            ('CSIT','Computer Science And Information Technology'),
            ('AIEE','Apllied Instrumental Electronic Engineering'),
            ('MARINE','Marine Engineering')
        )
        ),
        ('M.B.A',(
            ('FIN','Finance'),
            ('HR','Human Resource'),
            ('ACC','Accounts'),
            ('RD','Rural Development'),
            ('OL','Operation And Logistics'),
            ('MAR','Marketing')
        )
        ),
        ('Hotel Management',(
            ('FD','Front Desk'),
            ('KIT','Kitchen'),
            ('RS','Room Service'),
            ('FP','Food Production')
        )
        ),
        ('M.Sc',(
            ('PHY','Physics'),
            ('CHEM','Chemistry')
        )
        ),
        ('MCA','Master In Computer Application'),
        ('Diploma',(
            ('IT','Information Technology'),
            ('CIVIL','Civil'),
            ('ELE','Electrical'),
            ('MECH','Mechanical'),
        )
        ),
    ]
    yr = [ #? This is the choice of year 
        ('first','First Year'),
        ('second','Second Year'),
        ('third','Third Year'),
        ('fourth','Fourth Year'),
    ]
    sem =[ #? This is the choice of semister
        ('1','1st Semester'),
        ('2','2nd Semester'),
        ('3','3rd Semester'),
        ('4','4th Semester'),
        ('5','5th Semester'),
        ('6','6th Semester'),
        ('7','7th Semester'),
        ('8','8th Semester'),
    ]

    #course of  syallabus
    """
    cor_syl = {
        'CSE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'ETC' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                } 
        },
        'EE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'CE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'ME' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'CVE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'CSIT' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'AIEE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'MARINE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
                'fourth':{
                    '7' :
                    '8' :
                }
        },
        'FIN' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'HR' : {
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'ACC' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'RD' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'OL' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'MAR' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'FD' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :
                }
        },
        'KIT' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
        },
        'RS' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :
                }
        },
        'FP' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :
                }
        },
        'PHY' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'CHEM' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'MCA' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
        },
        'IT' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :

                }
        },
        'CIVIL' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :
                }
        },
        'ELE' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :
                }
        },
        'MECH' :{
                'first':{
                    '1' :
                    '2' :
                }
                'second':{
                    '3' :
                    '4' :
                }
                'third':{
                    '5' :
                    '6' :
                }
        }
    }
    """

    #basic information regarding the student... :))))
    sl_no =  models.IntegerField(serialize = True)
    #! This is the unique identification coloum
    reg_no = models.BigIntegerField(
        verbose_name = "Registration Number", 
        help_text = "It is the registration number allocated by BPUT", 
        primary_key = True, 
        unique = True, 
        editable = True,
        validators=[validate_registor_no,
            validate_register_content,]
    )
    college_id = models.CharField(
        verbose_name = "College Roll No",
        help_text = "It is the college assigned Roll No.",
        unique = True,
        max_length = 8
    )
    
    #! Personal detail section of student
    first_name = models.CharField(
            verbose_name = "First Name",
            help_text = "First Name of student",
            max_length = 30,
    )
    middle_name = models.CharField(
            verbose_name = "Middle Name",
            help_text = "Middle name of the student(if have or leave it.).",
            max_length = 30,
            blank = True,
    )
    last_name = models.CharField(
        verbose_name = "Last Name",
        help_text = "Last name of the student.",
        max_length = 30
    )
    dob = models.DateField(
        verbose_name="Date Of Birth",
        help_text = "Select your Date Of Birth",
    )
    join_year = models.DateField(
        verbose_name = "DOJ",
        help_text = "Select your date of join the college",
        default =  tz.now()
    )
    course = models.CharField(
        verbose_name = "Course Of Study",
        help_text = "Enter the Course of Student",
        choices= cor,
        default = 'B.Tech',
        max_length = 5
    )
    email = models.EmailField(
        verbose_name = 'E-Mail',
        help_text = "Enter Your E-Mail",
        max_length = 254
    )
    mobile1 = models.BigIntegerField(
        verbose_name='Personal Contact',
        help_text="Enter your Personal Contact",
        unique=True
    )
    mobile2 = models.BigIntegerField(
        verbose_name='Alternative Contact-I',
        help_text="Enter your First Aletnative Contact",
        blank=True,
        null= True
    )
    #! Acadimics Details

    semester = models.CharField(
        verbose_name = 'Semester',
        help_text = "select your Semester",
        max_length = 1,
        choices = sem,
        default = '1st Semester'
    )
    
    acc_year = models.CharField(
        verbose_name = 'Accademic Year',
        help_text = "Select your Accademic Year",
        max_length = 6,
        choices = yr,
        default = 'First Year'
    )
    #adding mentor detail
    #? This is having a foreign key from mentor-->mentors
    ment = models.ForeignKey(Mentor,
        on_delete = models.SET_NULL,
        verbose_name= "Mentor",
        help_text = "Select Your Mentor",
        null= True
    )

    #background process
    pay_id = models.CharField(
        verbose_name = "Payment Id",
        help_text = "This will store the unique paymnet id for the student",
        default = '',
        max_length = 40,
        editable = False,
        unique = True
        #? <passing_yr>@<reg_no><college_id>$<birth_year>_<birth_month>_<birth_date>!
    )

    def save(self,*args, **kwargs):
        "this will automatically add save the data when the save will invoke"
        #! i have used it due to auto genrating the pay_id
        
        if self.pay_id == "":
            data1 = self.join_year.year #now this is storeing the year of joining #! work pause
            data1 += 4 #now it is storeing the year of passing
            data2 = self.reg_no #it is storeing the BPUT registration number
            data3 = self.college_id #it is storeing the college id 
            data4 = self.dob.year #it is storeing the birth year
            data5 = self.dob.month #it is storeing the birth month
            data6 = self.dob.day#it is storeing the birth date

            self.pay_id = f'{data1}@{data2}{data3}${data4}_{data5}_{data6}!'
        super(Student,self).save()

    def __str__(self):
        "this is a to string for the model or entity -> students"
        return f'{self.reg_no} ]::[ {self.first_name} {self.middle_name} {self.last_name}'

class Parent(models.Model):
    "This the model or entity dealig with the parents of student and it is related to student"

    #! This section is the section of parents detail
    #this is the foreignKey  for the relation
    #? it consits of drop down we have to select the options.
    student = models.ForeignKey(Student,
         on_delete=models.CASCADE,
         verbose_name = "Student",
         help_text = 'Select the Students from the list given.(if not present add it)',
         default = ''
    )
    #!This is the father's datail for the selcted student
    father_name = models.CharField(
        verbose_name="Father's Name",
        help_text = "Name of Student's Father",
        max_length=60
    )
    father_occu = models.CharField(
        verbose_name="Fathers's Occupation",
        help_text = "Occupation of Student's Father",
        max_length = 60,
    )
    father_contact = models.BigIntegerField(
        verbose_name="Father's Contact No",
        help_text="Ckontact No of Student's Father"
    )

    #!This is the mother's detail for the selected student
    mother_name = models.CharField(
        verbose_name = "Mother's Name",
        help_text = "Name of Student's Mother",
        max_length = 60
    )
    mother_occu = models.CharField(
        verbose_name = "Mother's Occupation",
        help_text = "Occupation fo Student's Mother(edit it if she has a occupation)",
        max_length = 60,
        default = 'House Wife'#this will give defualt value to the filing data
    )
    mother_contact = models.BigIntegerField(
        verbose_name= "Mother's Contact No",
        help_text="Contact No Of Student's Mother"
    )
    
    def __str__(self):
        "to string for the parents model"
        return f"""
        Father ]:[ {self.father_name},
        Mother ]:[ {self.mother_name}
                """

class Document(models.Model):
    "This is the model or entity that is used store the documents of the student, documents -> student"

    #? use of <<<<<< pillo >>>>> library for the ImageFields... :)

    #! List of documents required for the student verification
    """
        # task completed #!<>
        # task incomplete #?<>

        #? Student Provided Information
        1. Student Photo  #!<added>
        2. 10th Pass Certificate #!<added>
        3. 10th Marksheet #!<added>
        4. 12th Pass Certificate #!<added>
        5. 12th Marketsheet #!<added>
        6. College Leaving Certifiacte  #!<added>
        7. Migration Certificate #!<added>
        8.OJEE Concent letter #!<added>
        #? Next task to add
        1. Returning admit card  #?<added>
    """
    #this is the section for adding all the information likke image store and all for document verification
    #? Current directory ]:[ C:\Users\kumar\Documents\mpDjango\src\student
    #? Saving to directory ]:[ C:\Users\kumar\Documents\mpDjango\src\DocStore\ (if the file present)
    #? Saving to directory ]:[ C:\Users\kumar\Documents\mpDjango\src\DocStore\None\no_image.png (if the file is not present)

    #this  section deals with the path of the documents
    
    #! This section is the section of documents details <It will for the exam department for integration of that document section -> student section>
    #this is the foreignkey for the relation
    #? It consists of drop down we have to select the colleg_id options <i.e CS170073>
    student = models.OneToOneField(Student,
    on_delete = models.CASCADE,
    help_text = "Select Registration Number with Name(if not present add it)",
    related_name = "Doc",
    )

    college_id = models.CharField(
        verbose_name = "Collge Id",
        help_text = "Enter the college roll number",
        unique = True,
        primary_key = True,
        max_length=8,
        editable = False
    )
    stud_img = models.ImageField(
        verbose_name="Identification Photo",
        help_text = "Upload your Passport Photo of Yours",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )
    ojee = models.ImageField( #ojee concent letter
        verbose_name="OJEE Concent Letter",
        help_text = "Upload the screenshot of your ojee Concent Letter",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )
    pass10_certi = models.ImageField( #10pass certificate
        verbose_name="10th Pass Certificate",
        help_text = "Upload your 10th Pass Certifiacte(scaned image)",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    ) 
    mark10_sheet = models.ImageField( #10 mark sheet
        verbose_name="10th Marksheet",
        help_text = "Upload your 10th Marksheet(scaned image)",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )
    pass12_certi = models.ImageField( #12th certificate
        verbose_name="12th Pass Certificate",
        help_text = "Upload your 12th Pass Certifiacte(scaned image)",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )
    mark12_sheet = models.ImageField( #12th marksheet
        verbose_name="12th Marksheet",
        help_text = "Upload your 12th Marksheet(scaned image)",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )
    clc = models.ImageField( #college leaving cetificate
        verbose_name="College Leaving Cetificate",
        help_text = "Upload your College Leaving Certificate",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )
    mig = models.ImageField( #Migration certificate
        verbose_name="Migration Certificate",
        help_text = "Upload your Migration Certificate",
        upload_to = upload_to,
        #default = 'DocStore/None/no_image.png',
        unique = True
    )

    def save(self,*args, **kwargs):
        "this wil store the student college id"
        this  = self.student # this is the link to the student for the data
        self.college_id = this.college_id
        super(Document, self).save()
    
    def __str__(self):
        "this is the to string for the modle or entity -> documents"
        return f'{self.college_id}'  

"""
     END NOTE ]::[
        i have created the fees app so lets look into the fees app for the deatails and set up the data base for it ..
        task completed students model ,parents models, documents model and setupping a detail realtionship among them.
        so 
        #todo 1.create the fees database
        #todo 2.app access record for better usage
        #todo 3.final linking and setting up for better project
        #! Sai ram and gud ni8....:) 
"""

"""
#!TECHNICAL NOTE <CASCADE>
    < on_delete = models.CASCADE >
        Is the process when we delete an entity the other entity having a relationship with it, will be deleted
        for the above situation ]::[ 
                   ==============      =============
                   || Student  ||  --> || Parents ||
                   ==============      =============
                        ||
                        ||                  when we ll delete a student from student_entity then all related entity  to it will deleted.
                        \/
                    ===============
                    || Documents ||
                    ===============
#! TECHNICAL NOTE save
    
    def save(self):
        "this is used to auto populate"
        if '17' in str(self.reg):
            self.t_options = 'STD'
        elif '71' in str(self.reg):
            self.t_options = 'TCH'
        super(lastTest, self).save()
     this will help in auto populate the field in the model
#! TECHNICAL NOTE TO FIX THE DYNAMIC LOCATION USING THE OS MODULE
    USE os.listdir() to find the list of files present in the file
    USE max(os.listdir(<path>), key= os.path.getctime) #? to get the recent time of the file created
"""