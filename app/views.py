from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import SignUpForm,OrderForm
from .models import Order
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def base(request):
    return render(request,"base.html")


def admin_login(request):
	error = ""
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d = {'error' : error}
	return render(request,'adminlogin.html',d)

def admindashboard(request):
    return render(request,"admin.html")
    
def admin_logout(request):
    if not request.user.is_staff:
	    return redirect('admin_login')
    logout(request)
    return redirect('admin_login')


def adminread(request):
    adminread = Order.objects.all()
    return render(request,"adminread.html",{'adminread':adminread})


def adminupdate(request,id):
    upd1=Order.objects.get(id=id)
    update=OrderForm(request.POST or None,request.FILES or None,instance=upd1)
    if update.is_valid():
        messages.success(request,"Form has been Updated.")
        update.save()
    return render(request,"adminupdate.html",{"adminupdate":update})


# def emailsent(request):
#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         email = request.POST["email"]

#         user = User.objects.create_user(
#             username = username,
#             password = password,
#             email = email
#         )
#         login(request,user)
#         subject = 'welcome to GFG world'
#         message = f'Hi {user.username}, thank you for registering in.'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [user.email, ]
#         send_mail( subject, message, email_from, recipient_list )
#         return redirect(base)


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered Successfully")
            # return redirect(emailsent)
    else:
        form = SignUpForm()
    return render(request,"signup.html",{'form':form})


@login_required
def order(request):
    form = OrderForm()
    if request.method == "POST":
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            orderform.save()
            messages.success(request, "Form has been submitted.")
    return render(request, "order.html", {'form': form})

@login_required
def readorder(request):
    read = Order.objects.all()
    return render(request,"read.html",{'read':read})


@login_required
def updateorder(request,id):
    upd=Order.objects.get(id=id)
    update=OrderForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        messages.success(request,"Form has been Updated.")
        update.save()
    return render(request,"update.html",{"update":update})

@login_required
def deleteorder(request,id):
    order_del = Order.objects.get(id=id)
    order_del.delete()
    return redirect(readorder)
    
