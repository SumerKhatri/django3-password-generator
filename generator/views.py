from django.shortcuts import render
from django.http import *
import random
import logging
# Create your views here.

# Added RequestContext
def home(request):
    #return HttpResponse('Hello There Friend!')
    passwords={'pass1':123}
    return render(request,'generator/home.html',passwords)
def Profile(request):
    return HttpResponse('<h1>This is your Profile!<h1>')
def about(request):
    info="Hey,This website helps you quickly create a password randomly with all the requirements given as input.So just sit back and relax,we will create a new password for you!This is Sumer Khatri and team signing off!"
    return render(request,'generator/about.html',{'about_page':info})
def password(request):
    thepassword=""
    lower_chars='abcdefghijklmnopqrstuvwxyz'
    upper_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_chars="!@#$%^&*"
    numbers="1234567890"
    finalStr=lower_chars
    len=int(request.GET.get('length'))
    if request.GET.get('special')!=None:
        finalStr=finalStr+special_chars
    if request.GET.get('uppercase')!=None:
        finalStr=finalStr+upper_chars
    if request.GET.get('number')!=None:
        finalStr=finalStr+numbers

    characters=list(finalStr)


    for x in range(len):
        thepassword=thepassword+random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
