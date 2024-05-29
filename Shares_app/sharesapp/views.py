from django.shortcuts import render,redirect
from django.contrib.auth.models import User         
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout    #----  to authenticate  plane password to encrypted password and check with existing encrypted passord record
from django.contrib.auth.decorators import login_required    #---- decorator login must required throughout all urls
from .models import UserShareDetails,UserLogDetails
import time

def base(request):
    return render(request,'sharesapp/base.html')

def signup_page(request):
    if request.method=="POST":
        username    =   request.POST.get('username')
        first_name  =   request.POST.get('first_name')
        last_name   =   request.POST.get('last_name')
        password    =   request.POST.get('password')

        user= User.objects.filter(username = username)                #username is already existed then redirect to sign_up and show messages 
        if user.exists():
            messages.info(request, 'Username already taken...!!')
            return redirect("SIGN_UP")
                
        userobj=User.objects.create( 
            username     =  username,
            first_name   =  first_name,
            last_name    =  last_name)
        
        userobj.set_password(password)              #-----> Set_password used to encrypt typed password
        userobj.save()
        if userobj.save():
            messages.info(request, 'User successfully registered ...!!')
        time.sleep(2)
        
        return redirect ("LOG_IN")  
    return render(request,'sharesapp/signup.html')

def login_page(request):
    if request.method=="POST":
        username    =   request.POST.get('username')
        password    =   request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid Username !!')
            return redirect('LOG_IN')
        user=authenticate(username=username,password=password)      #--->Authenticate both attributes --->if it valid it return both --->if it invalid then it return none
        if user is None:                                               #user object 
            messages.info(request, 'Invalid Password!!')
            return redirect('LOG_IN')
        else:
            login(request,user)                          #------> We need logged user name----> {{ request.user }} --->in relation models
            return redirect("USER_LIST")                 #---------------> INDEX page of the App--> UserNameslist
    return render(request,'sharesapp/login.html')

def logout_page(request):
    logout(request)                      
    return redirect('LOG_IN')

@login_required(login_url="LOG_IN")
def UsersList(request,id=None): 
    if request.method=="GET" and id==None:
        data=User.objects.all()
    return render(request,'sharesapp/user_list.html',{'userlist':data})

@login_required(login_url="LOG_IN") 
def shareslist(request,id=None,s_id=None):     
    userdata =UserShareDetails.objects.all().filter(user_id_id=id)
    
    if request.method=="POST" and id!=None: 
        companyshare  =   request.POST.get('companyshare')
        quantity      =   request.POST.get('quantity')
        price         =   request.POST.get('price')
        date          =   request.POST.get('date')
        print(companyshare,quantity,price,id)
        shareobj=UserShareDetails(user_id_id=id,date = date, companyshare = companyshare,quantity = quantity,price = price)
        #print(shareobj.s_id,shareobj.date,shareobj.companyshare,shareobj.quantity,shareobj.price,shareobj.user_id_id)
        remark='Purchased + $'
        changes=(shareobj.date,shareobj.companyshare,shareobj.quantity,shareobj.price,shareobj.user_id_id)
        addlog=UserLogDetails(uid=id,remark=remark,changes=changes)
        addlog.save()
        shareobj.save()
        return redirect('SHARE_LIST',id)
    return render(request,'sharesapp/shares_list.html',{'data':userdata,'id':id})

@login_required(login_url="LOG_IN")
def edit_share(request,id=None,s_id=None):
    if request.method=="GET" and id!=None and s_id!=None:
        eobj=UserShareDetails.objects.get(s_id=s_id)
        #print(eobj.s_id,eobj.date,eobj.companyshare,eobj.quantity,eobj.price,eobj.user_id_id)
        ul=UserLogDetails()   
        return render(request,'sharesapp/edit_share.html',{'eobj':eobj,'uid':id})

    if request.method=="POST" and id!=None and s_id!=None: 
        date          =   request.POST.get('date')
        companyshare  =   request.POST.get('companyshare')
        quantity      =   request.POST.get('quantity')
        price         =   request.POST.get('price')
        up_obj=UserShareDetails(s_id=s_id,date=date,companyshare=companyshare,quantity=quantity,price=price,user_id_id=id)
        #print(up_obj.s_id,up_obj.date,up_obj.companyshare,up_obj.quantity,up_obj.price,up_obj.user_id_id)
        remark='Update $'
        changes=(up_obj.date,up_obj.companyshare,up_obj.quantity,up_obj.price)
        editlog=UserLogDetails(uid=id,remark=remark,changes=changes)
        editlog.save()
        up_obj.save()
        return redirect('SHARE_LIST',id)

@login_required(login_url="LOG_IN")   
def del_share(request,id=None,s_id=None):
    if request.method=="GET" and s_id!=None :
        delobj=UserShareDetails.objects.get(pk=s_id)
        #print(delobj.price,delobj.user_id_id)
        remark='Sold - $'
        changes=(delobj.date,delobj.companyshare,delobj.quantity,delobj.price)
        editlog=UserLogDetails(uid=id,remark=remark,changes=changes)
        editlog.save()
        delobj.delete()
        return redirect('SHARE_LIST',id)

@login_required(login_url="LOG_IN")
def user_logs(request,id=None):
    if request.method=="GET" and id!=None :
        userlogs=UserLogDetails.objects.all().filter(uid=id)                #filter log according to user id
    return render(request,'sharesapp/user_logs.html',{'userlogs':userlogs})