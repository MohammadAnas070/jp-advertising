from django.shortcuts import render, redirect,HttpResponse
from user.models import *
from django.contrib.auth.models import User
from user.models import Profile
from myadmin.models import *
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail  
from .helper import send_forget_password_mail_to_agency
import os
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.db import IntegrityError



def home(request):
    id = request.user.id
    if id == None:
        result1 = Upload_product.objects.all()
        context = {'result1':result1}
        
        return render(request,'user/dashboard.html',context)

    
    else:
        id = request.user.id
        result1 = Upload_product.objects.all()
        result = User.objects.get(pk=id)
        context={'result':result,'result1':result1}
        return render(request,'user/dashboard.html',context)
#-----------------------------------------------------------------
def contact(request):
    context={}
    return render(request,'user/contact.html',context)

def store_cust_inquiry(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    message = request.POST['message']
    

    Customer_inquiry.objects.create(name=name,email=email,contact=contact,message=message)
    return redirect('/user/contact')

def inquiry_read(request):
    result = Customer_inquiry.objects.all()
    context = {'result':result}
    return render(request,'myadmin/cust_inquiry_read.html',context)

def inquiry_delete(request,id):
    result = Customer_inquiry.objects.get(pk=id)
    result.delete()
    return redirect('/user/inquiry_read')
#------------------------------------------------------------------------
def login(request):
    context={}
    return render(request,'user/login.html',context)


def login_check(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        result1 = User.objects.get(username=username)
        result = auth.authenticate(request, username=username,password=password)
        if result1.first_name == "" or result1.is_staff != 0:
            messages.success(request, 'Invalid Username Or Password or You are Not Authorised User !!')
            print('Invalid Username Or Password or You are Not Authorised User')
            return redirect('/user')
        if result is None:
            messages.success(request, 'Invalid Username or Password')
            print('Invalid Username or Password')
            return redirect('/user/')
        else:
            auth.login(request, result)
            return redirect('/user/home')

    except ObjectDoesNotExist:
         my_object = None
         messages.success(request, 'Invalid Username or not Found Username')
         print('Invalid Username or You are not Admin')
         return redirect('/user/')
#-----------------------------------------------------------------------------
def register(request):
    context={}
    return render(request,'user/register.html',context)

def user_store(request):
    fname  = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    #Profile Model
    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    dob  = request.POST['dob']

    try:
        if password != cpassword :
            messages.success(request, 'Password Missmatch')
            return redirect('/user/register')
            print ('Missmatch Password')



            
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already taken')
            return redirect('/user/register')
        else:
            result = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
            Profile.objects.create(contact=contact,address=address,gender=gender,user_id=result.id)
            password_all.objects.create(user_password=password,user_id=result.id)
            return redirect('/user/')
            
            

    except IntegrityError as e:
        messages.warning(request, 'Username already taken')
        return redirect('/user/register')
    

    
        # except ObjectDoesNotExist:
        #     myobject = None
        #     messages.success(request, 'Invalid Username or You are not Admin')
        #     print('Invalid Username or You are not Admin')
        #     return redirect('/register/')
   
    # User Model
    
       
def user_read(request):
    result = Customer_register.objects.all()
    context = {'result':result}
    return render(request,'myadmin/user_read.html',context)

#---------------------------------------------------------
def logout(request):
    auth.logout(request)
    return redirect('/user/home')
#--------------------------------------------------------

def feedback(request):
    context = {}
    return render(request,'user/feedback.html',context)

def store_cust_feedback(request):
    try:
        # rating = request.POST['rating']
        message = request.POST['message']
        id = request.user.id
        Customer_feedback.objects.create(message=message,user_id=id)
        return redirect('/user/feedback')
    except IntegrityError:

        messages.success(request, 'You had already give a feedback')
        return redirect('/user/feedback')
    

def feedback_read(request):
    result = Customer_feedback.objects.all()
    context = {'result':result}
    return render(request,'myadmin/cust_feedback_read.html',context)

def feedback_delete(request,id):
    result = Customer_feedback.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/feedback_read')
#-----------------------------------------------------------------
def aboutus(request):
    context = {}
    return render(request,'user/aboutus.html',context)
#-------------------------------------------------------
def userprofile(request,id):
    fkid = request.user.id
    result = User.objects.get(pk=id)
    result1 = Profile.objects.get(user_id = fkid)
    context = {'result1':result1}
    return render(request,'user/userprofile.html',context)

def profile(request,id):
    fkid = request.user.id
    result = User.objects.get(pk=id)
    result1 = Profile.objects.get(user_id = fkid)
    context = {'result1':result1}
    
    return render(request,'user/profile.html',context)

def userprofile_update(request,id):
    user = request.user.id
    result = Profile.objects.get(pk=id)


    data = {
                'fname': request.POST['fname'],
                'lname': request.POST['lname'],
                'email': request.POST['email'],
                'username': request.POST['username']

            }

    data1 = {
                'contact': request.POST['contact'],
                'address': request.POST['address'],
                
                
                'gender': request.POST['gender']

    }

    result = User.objects.update_or_create(pk=user, defaults=data)
    Profile.objects.update_or_create(pk=id, defaults=data1)
    return redirect('/user/home')


def profile_image(request, id):
    user = request.user.id
    result = Profile.objects.get(user_id=user)
    myfile = request.FILES['f']
    mylocation = os.path.join(settings.MEDIA_ROOT,'profile')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name, myfile)

    data = {
            'profile_image' : myfile.name
    }
    Profile.objects.update_or_create(user_id=user, defaults=data )
    return redirect('/user/home')
#------------------------------------------------------------------
def upload_product(request,id):
    result = Category.objects.all()
    result1 = Subcategory.objects.all()
    context = {'result':result,'result1':result1}

    return render(request,'user/user_upload_product.html',context)

def upload_product_store(request,id):
    user = request.user.id
    result1 = Profile.objects.get(user_id=user)
    contact = result1.contact
    productname = request.POST['productname']
    title = request.POST['title']
    category = request.POST['category']
    subcategory = request.POST['subcategory']
    price = request.POST['price']
    description = request.POST['description']
    largedes = request.POST['largedes']
    

    myfile = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name, myfile)

    Upload_product.objects.create(productname=productname,title=title,category_id=category,subcategory_id=subcategory,price=price,description=description,largedes=largedes,image=myfile.name,user_id=user,contact=contact)
    return render(request,"user/user_upload_product.html")

#-------------------------------------------------------------------
def ForgetPassword(request):

    
    return render(request,'user/forgetpassword.html')


def ForgetPassword_chk(request):
    username = request.POST['username']
    result = User.objects.get(username=username)
    user = result.id
    if result is None:
        messages.success(request, 'Invalid Username ')
        print('Invalid Username Or Password')
        return redirect('/user/ForgetPassword')
    else:
        email = result.email
        fname = result.first_name
        lname = result.last_name
        result1 = password_all.objects.get(user_id=user)
        password = result1.user_password
        
        send_mail(
            'Forget Password',
            'Old Password {password}',
            'shaikhsohail1131@gmail.com',
            [email],
            fail_silently=False,
            )
        send_forget_password_mail_to_agency(email,password,fname,lname)
        messages.success(request, 'Check Your Mail ')
    
    
    return redirect('/user/ForgetPassword')
#--------------------------------------------------------------------------------------
def product_view(request,id):
    result = Upload_product.objects.get(pk=id)
    upid = result.id
    price = result.price
    productname = result.productname
    title = result.title 
    description = result.description
    image = result.image
    contact = result.contact
    largedes= result.largedes
    
    user_id = result.user_id
    category_id = result.category_id
    subcategory_id = result.subcategory_id

    request.session['price'] = price
    request.session['productname'] = productname
    request.session['title'] = title
    request.session['description'] = description
    request.session['largedes'] = largedes
    request.session['user_id'] = user_id
    request.session['category_id'] = category_id
    request.session['subcategory_id'] = subcategory_id
    request.session['image'] = image
    request.session['upid'] = upid
    request.session['contact'] = contact
    

    context = {'result':result}
    return render(request,'user/product_view.html',context)
#------------------------------------------------------------------------------
def cart(request):
    user = request.user.id
    result = Cart_store.objects.filter(user_id=user)
    context ={'result':result}
    return render(request,'user/cart.html',context)

def cart_store(request,id):
    try:
        user = request.user.id
        productname = request.session['productname']
        title = request.session['title']
        price = request.session['price']
        description = request.session['description'] 
        largedes = request.session['largedes']
        image = request.session['image']
        upid = request.session['upid']
        contact = request.session['contact']
        Cart_store.objects.create(productname=productname,title=title,price=price,description=description,largedes=largedes,image=image,uploader_id=upid,sellercontact=contact,user_id=user)
        return redirect('/user/cart')

    except IntegrityError:
        return redirect('/user/')
        
    

def cart_delete(request,id):
    result = Cart_store.objects.get(pk=id)
    result.delete()
    return redirect('/user/cart')
#-----------------------------------------------------------------------------
def myproduct(request):
    user = request.user.id
    result = Upload_product.objects.filter(user_id=user)
    context ={'result':result}
    return render(request,'user/myproduct.html',context)

def myproduct_update(request,id):
    user = request.user.id
    result = Upload_product.objects.get(pk=id)
    data = {
                'productname': request.POST['productname'],
                'title': request.POST['title'],
                'price': request.POST['price'],
                'description': request.POST['description'],
                'largedes' :request.POST['largedes'],

            }
    result = User.objects.update_or_create(pk=user, defaults=data)
    return redirect('/user/home')

def myproduct_delete(request,id):
    result = Upload_product.objects.get(pk=id)
    result.delete()
    return redirect('/user/myproduct')
#-----------------------------------------------------------------------------------
def search(request):

    try:
        search = request.POST['search']
        result= Subcategory.objects.get(subcategory_name=search)
        subcategory = result.subcategory_name
        result1 = Upload_product.objects.filter(subcategory_id=result.id)
        context={'result1':result1}
        return render(request,'user/dashboard.html',context)

    except :
        pass

#--------------------------------------------------------------------------
def category(request):
    result1 = Upload_product.objects.all()
    context ={'result1':result1}
    return render(request,'user/category.html',context)

def category_electronics(request):
    search = '1'
    result= Category.objects.get(pk=search)
    result1 = Upload_product.objects.filter(category_id=result.id)
    context={'result1':result1}
    return render(request,'user/dashboard.html',context)

def category_furniture(request):
    search = '2'
    result= Category.objects.get(pk=search)
    result1 = Upload_product.objects.filter(category_id=result.id)
    context={'result1':result1}
    return render(request,'user/dashboard.html',context)

def category_clothes(request):
    search = '3'
    result= Category.objects.get(pk=search)
    result1 = Upload_product.objects.filter(category_id=result.id)
    context={'result1':result1}
    return render(request,'user/dashboard.html',context)

def category_vehicles(request):
    search = '4'
    result= Category.objects.get(pk=search)
    result1 = Upload_product.objects.filter(category_id=result.id)
    context={'result1':result1}
    return render(request,'user/dashboard.html',context)

    
def category_design_art(request):
    search = '5'
    result= Category.objects.get(pk=search)
    result1 = Upload_product.objects.filter(category_id=result.id)
    context={'result1':result1}
    return render(request,'user/dashboard.html',context)

def category_book(request):
    search = '6'
    result= Category.objects.get(pk=search)
    result1 = Upload_product.objects.filter(category_id=result.id)
    context={'result1':result1}
    return render(request,'user/dashboard.html',context)
#------------------------------------------------------------------------------------

def changepass(request):
    return render(request,'user/changepass.html')

def ChangePassword_chk(request):
    user_id = request.user.id
    username = request.POST['username']
    passwd = request.POST['password']
    cpasswd = request.POST['cpassword']

    if passwd != cpasswd:
        messages.success(request, 'Confirm password does not match')
        return redirect('/user/changepass')
    if user_id is None:
        messages.success(request, 'Login First to Change Password')
        return redirect('/user/')

    else :
        u= User.objects.get(username=username)
        u.set_password(passwd)
        u.save()
        data = {
                'user_password': passwd
                }
        password_all.objects.update_or_create(user_id=user_id, defaults=data)
        messages.success(request, 'Successfully Updated !! \nlogin first')
        return redirect('/user/')