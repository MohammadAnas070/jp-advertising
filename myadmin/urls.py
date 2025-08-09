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
from myadmin import views
from.views import *

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('admin_login_check', views.admin_login_check, name='admin_login_check'),
    
    path('logout', views.logout, name='logout'),
    path('form', views.form, name='form'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('user', views.user, name='user'),
    path('user_viewmore/<int:id>', views.user_viewmore, name='user_viewmore'),
    
    path('cust1', views.cust1, name='cust1'),
    path('cust2', views.cust2, name='cust2'),
    path('agency', views.agency, name='agency'),
    path('feedback', views.feedback, name='feedback'),
    path('order', views.order, name='order'),


    path('category',views.category,name='category'),
    path('store_category',views.store_category,name='store_category'),
    path('category_read',views.category_read,name='category_read'),
    path('category_edit/<int:id>',views.category_edit,name='category_edit'),
    path('category_delete/<int:id>',views.category_delete,name='category_delete'),
    path('category_update/<int:id>',views.category_update,name='category_update'),


    path('sub_category',views.sub_category,name='sub_category'),
    path('store_subcategory',views.store_subcategory,name='store_subcategory'),
    path('subcategory_read',views.subcategory_read,name='subcategory_read'),
    path('subcategory_delete/<int:id>',views.subcategory_delete,name='subcategory_delete'),
    path('subcategory_update/<int:id>',views.subcategory_update,name='subcategory_update'),
    path('subcategory_edit/<int:id>',views.subcategory_edit,name='subcategory_edit'),

    path('view_all_product',views.view_all_product,name='view_all_product'),
    path('viewmore_all_product/<int:id>',views.viewmore_all_product,name='viewmore_all_product'),
    path('view_delete/<int:id>',views.view_delete,name='view_delete'),
    path('admin_upload_product/<int:id>', views.admin_upload_product, name='admin_upload_product'),
    path('admin_upload_product_store/<int:id>', views.admin_upload_product_store, name='admin_upload_product_store'),
    path('myproduct', views.myproduct, name='myproduct'),
   

    path('city',views.city,name='city'),
    path('state',views.state,name='state'),

    path('pdf/', GeneratePdf.as_view()),
    path('pdf2/', GeneratePdf2.as_view()),
    path('pdf3/', GeneratePdf3.as_view()),



]
