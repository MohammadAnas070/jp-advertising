"""JpAdvertise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('/', views.home, name='home'),   
   #----------------------------------------------------------------- 
    path('contact', views.contact, name='contact'),
    path('store_cust_inquiry', views.store_cust_inquiry, name='store_cust_inquiry'),
    path('inquiry_read', views.inquiry_read, name='inquiry_read'),
    path('inquiry_delete/<int:id>', views.inquiry_delete, name='inquiry_delete'),
   #-------------------------------------------------------------------
    path('register', views.register, name='register'),
    path('register', views.register, name='register'),
    path('user_store', views.user_store, name='user_store'),
    #---------------------------------------------------
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
   #---------------------------------------------------------------------------- 
    path('feedback', views.feedback, name='feedback'),
    path('store_cust_feedback', views.store_cust_feedback, name='store_cust_feedback'),
    path('feedback_read', views.feedback_read, name='feedback_read'),
    path('feedback_delete/<int:id>', views.feedback_delete, name='feedback_delete'),
   #------------------------------------------------------------------------------ 
    path('aboutus', views.aboutus, name='aboutus'),
   #------------------------------------------------------------------------------ 
    path('profile/<int:id>', views.profile, name='profile'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),

    path('userprofile_update/<int:id>', views.userprofile_update, name='userprofile_update'),
    path('upload_product/<int:id>', views.upload_product, name='upload_product'),
    path('upload_product_store/<int:id>', views.upload_product_store, name='upload_product_store'),
    path('profile_image/<int:id>', views.profile_image, name='profile_image'),
      
   #------------------------------------------------------------------------------ 
   path('ForgetPassword', views.ForgetPassword, name='ForgetPassword'),
   path('ForgetPassword_chk', views.ForgetPassword_chk, name='ForgetPassword_chk'),
   path('product_view/<int:id>', views.product_view, name='product_view'),
   #------------------------------------------------------------------------------
   path('cart', views.cart, name='cart'),
   path('cart_store/<int:id>', views.cart_store, name='cart_store'),
   path('cart_delete/<int:id>', views.cart_delete, name='cart_delete'),
   #--------------------------------------------------------------------------------- 
   path('myproduct', views.myproduct, name='myproduct'),
   path('myproduct_delete/<int:id>', views.myproduct_delete, name='myproduct_delete'),
   path('myproduct', views.myproduct, name='myproduct'),
   path('search',views.search, name='search'), 

   path('category',views.category, name='category'),
   path('category_electronics',views.category_electronics, name='category_electonics'),
   path('category_furniture',views.category_furniture, name='category_furniture'),
   path('category_clothes',views.category_clothes, name='category_clothes'),
   path('category_vehicles',views.category_vehicles, name='category_vehicles'),
   path('category_design_art',views.category_design_art, name='category_design_art'),
   path('category_book',views.category_book, name='category_book'),
  
   path('changepass',views.changepass, name='changepass'),
   path('ChangePassword_chk',views.ChangePassword_chk, name='ChangePassword_chk'),
   

   ]
