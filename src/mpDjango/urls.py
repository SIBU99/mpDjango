"""mpDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from login.views import login_view,home_view
from student.views import PrePaymnetSlipView, PrePaymentRecieptView, TransactionView, StudHomeView, FeesView, WhoamiView
from tester.views import TestView
from mentor.views import DashView, MentHomeView, whoIam, displayStudent

urlpatterns = [
    path('student/payment2/',PrePaymentRecieptView, name = 'pay2'),
    path('student/payment/',PrePaymnetSlipView, name = 'pay'),
    path('login/',login_view, name= 'login'),
    path('admin/', admin.site.urls),
    path('test/',TestView, name='test' ),
    path('mentor/home/',MentHomeView, name = 'ment_home'),
    path('mentor/information/<int:RegNO>', displayStudent, name = 'display_stud' ),
    path('mentor/whoiam/', whoIam, name = 'miam'),
    path('mentor/dash/',DashView, name='Dash' ),
    path('response/',TransactionView, name='Respo'),
    path('student/home/',StudHomeView, name='stud_home'),
    path('student/fess/',FeesView, name='fees'),
    path('student/whoiam/',WhoamiView, name = 'iam'),
    path('',home_view, name='home' )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
