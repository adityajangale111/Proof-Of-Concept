from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.base,name='base'),
    path('accounts/',include("django.contrib.auth.urls")),
    path('admin_login/',views.admin_login,name='admin_login'),
    path("adminhome/",views.admindashboard,name="adminhome"),
    path('adminlogout/',views.admin_logout,name='adminlogout'),
    path('adminread/',views.adminread,name='adminread'),
    path('signup/',views.SignUp,name='signup'),
    # path('emailsent/',views.emailsent,name='emailsent'),

    path("order",views.order,name='order'),
    path('readorder/',views.readorder,name='readorder'),
    # path('updateorder/<int:id>',views.updateorder,name='updateorder'),
    path('updateorder/<int:id>/update/',views.updateorder,name='updateorder'),
    path('deleteorder/<int:id>/delete/',views.deleteorder,name='deleteorder'),
    path('adminupdate/<int:id>/',views.adminupdate,name='adminupdate'),
]
