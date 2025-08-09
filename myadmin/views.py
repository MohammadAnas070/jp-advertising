from django.shortcuts import render, redirect
from myadmin.models import *
from user.models import *
from django.contrib.auth.models import User
from user.models import Profile
from myadmin.models import *
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.generic import View
from .helpers import html_to_pdf

import os


def dashboard(request):
    request.session.setdefault('visitor_count', 0)
    request.session['visitor_count'] += 1
    user_count=User.objects.count()
    upload_product=Upload_product.objects.count()
    category = Category.objects.count()
    subcategory = Subcategory.objects.count()
    print(upload_product)
    id = request.user.id 
    if id == None:
        return redirect('/myadmin/')
    else:
        visitor_count = request.session['visitor_count']
        return render(request, 'myadmin/dashboard.html', {'visitor_count': visitor_count,'user_count':user_count,'upload_product':upload_product,'category':category,'subcategory':subcategory})



    # Pass the visitor count to the template
    #--------------------------------------------------------------------
def login(request):
    context={}
    return render(request,'myadmin/login.html',context)


def admin_login_check(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        result1 = User.objects.get(username=username)

        result = auth.authenticate(request, username=username,password=password)

        if result.is_staff == 0 :
        # if result.is_superuser == 1:# and result is None:
            messages.success(request, 'Invalid Username or You are not Admin')
            print('Invalid Username or You are not Admin')
            return redirect('/myadmin/')
        else:
            auth.login(request, result)
            return redirect('/myadmin/dashboard')

    except ObjectDoesNotExist:
        myobject = None
        messages.success(request, 'Invalid Username or You are not Admin')
        print('Invalid Username or You are not Admin')
        return redirect('/myadmin/')
     
    #--------------------------------------------------------------------
def logout(request):
    auth.logout(request)
    return redirect('/user/home')   
#--------------------------------------------------------------------
def form(request):
    context = {}
    return render(request,'myadmin/form.html',context)

def inquiry(request):
    context = {}
    return render(request,'myadmin/inquiry.html',context)

def user(request):
    result = Profile.objects.all()
    context = {'result':result}
    return render(request,'myadmin/user.html',context)

def user_viewmore(request,id):
    result = Profile.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/user_viewmore.html',context)

def agency(request):
    context = {}
    return render(request,'myadmin/agency.html',context)

def feedback(request):
    context = {}
    return render(request,'myadmin/feedback.html',context)

def order(request):
    context = {}
    return render(request,'myadmin/order.html',context)
#--------------------------------------------------------------------
def cust1(request):
    context = {}
    return render(request,'myadmin/user_info/john.html',context)

def cust2(request):
    context = {}
    return render(request,'myadmin/user_info/mark.html',context)
#--------------------------------------------------------------------
def category(request):
    context = {}
    return render(request,'myadmin/category.html',context)

def store_category(request):
    cat_name = request.POST['category']

    Category.objects.create(cat_name=cat_name)

    return redirect('/myadmin/category')

def category_read(request):
    result = Category.objects.all()
    context = {'result':result}
    return render(request,'myadmin/category_read.html',context)


def category_edit(request,id):
    result = Category.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/category_edit.html',context)


def category_delete(request,id):
    result = Category.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/category_read')

def category_update(request,id):
    data = {
                'cat_name': request.POST['category']
    }

    Category.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/category_read')
#--------------------------------------------------------------------
def sub_category(request):
    catagories = Category.objects.all()
    context = {'catagories':catagories}
    return render(request,'myadmin/sub_category.html',context)

def store_subcategory(request):
    subcategory_name = request.POST['subcategory']
    category = request.POST['category']

    Subcategory.objects.create(subcategory_name=subcategory_name,category_id=category)

    return redirect('/myadmin/sub_category')


def subcategory_read(request):
    result = Subcategory.objects.all()
    
    context = {'result':result}
    return render(request,'myadmin/subcategory_read.html',context)

def subcategory_delete(request,id):
    result = Subcategory.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/subcategory_read')

def subcategory_edit(request,id):
    result = Subcategory.objects.get(pk=id)
    result1 = Category.objects.all()

    context = {'result':result,'result1':result1}
    return render(request,'myadmin/subcategory_edit.html',context)

def subcategory_update(request,id):

    data = {
                'subcategory': request.POST['subcategory'],
                'category_id': request.POST['category']
    }

    Subcategory.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/subcategory_read')
#--------------------------------------------------------------------
def city(request):
    context = {}
    return render(request,'myadmin/city.html',context)

def state(request):
    context = {}
    return render(request,'myadmin/state.html',context)
#--------------------------------------------------------------------
def view_all_product(request):
    result = Upload_product.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_all_product.html',context)

def viewmore_all_product(request,id):
    result = Upload_product.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/viewmore_all_product.html',context)

def view_delete(request,id):
    result = Upload_product.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_all_product')

def admin_upload_product(request,id):
    result = Category.objects.all()
    result1 = Subcategory.objects.all()
    context = {'result':result,'result1':result1}

    return render(request,'myadmin/admin_upload_product.html',context)

def admin_upload_product_store(request,id):
    user = request.user.id
    
    contact = request.POST['contact']
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
    return render(request,"myadmin/admin_upload_product.html")

def myproduct(request):
    user = request.user.id
    result = Upload_product.objects.filter(user_id=user)
    context ={'result':result}
    return render(request,'myadmin/myproduct_store.html',context)
#------------------------------------------------------------------------

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        query = request.user.id
        result = Upload_product.objects.all()
        context = {'result':result}
        # getting the template
        pdf = html_to_pdf('report1.html',context)
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePdf2(View):
    def get(self, request, *args, **kwargs):
        query = request.user.id
        result = Category.objects.all()
        context = {'result':result}
        # getting the template
        pdf = html_to_pdf('report2.html',context)
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePdf3(View):
    def get(self, request, *args, **kwargs):
        query = request.user.id
        result = Subcategory.objects.all()
        context = {'result':result}
        # getting the template
        pdf = html_to_pdf('report3.html',context)
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')