from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('bulletin:notices'))
    if request.method == 'POST':
	form = Login(request.POST)
	if form.is_valid():
	    username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
	    if user is not None:
                login(request, user)
		return HttpResponseRedirect(reverse('bulletin:notices'))
	    else :
		return HttpResponse("Input Invalid")
    else:
        form = Login()
    	return render(request, 'bulletin/index.html',{'form':form,})

def logout(request):
    logout(request)
    return render(request, 'bulletin/logout.html')

@login_required(login_url='/bulletin/')
def notice(request):
	""" 
	Returns the lists of notices in sorted order
	"""
	latest_notice_list = Notice.objects.order_by('-upload')
	template = loader.get_template('bulletin/notices.html')
	context = {
	    'latest_notice_list': latest_notice_list,
	}
	return HttpResponse(template.render(context, request))
	

@login_required(login_url='/bulletin/')
def notice_detail(request, notice_id):
        notice = get_object_or_404(Notice, pk=notice_id)
	expirydate= notice.expiry_date
	if datetime.today() > expirydate:
	    status = 'expired'
	else:
	    status= 'active'
	return render(request, 'bulletin/notice_detail.html', {'notice': notice, 'status':status})
	
@login_required(login_url='/bulletin/')
def student(request):
    student_list = Student.objects.all().order_by('enr_no')
    template = loader.get_template('bulletin/students.html') 
    context = {                                           
        'student_list': student_list,         
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/bulletin/')
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'bulletin/student_detail.html', {'student': student}) 

@login_required(login_url='/bulletin/')
def category(request):
    category_list = Category.objects.all().order_by('name')
    template = loader.get_template('bulletin/categories.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))    

@login_required(login_url='/bulletin/')
def category_notice(request,category_id):
    category = get_object_or_404(Category, pk=category_id)
    notice_list = Notice.objects.all().filter(category = category_id)
    template = loader.get_template('bulletin/category_notice.html')
    context = {                                           
       'notice_list': notice_list,         
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/bulletin/')
def subscription(request,student_id):
    subscribed_list = Subscription.objects.all().filter(student__id = student_id)
    template = loader.get_template('bulletin/subscribed.html')
    context = {                                           
        'subscribed_list': subscribed_list,         
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/bulletin/')
def starred(request,student_id):
    notice_list = SNlink.objects.all().filter(student__id = student_id)
    template = loader.get_template('bulletin/starred.html')
    context = {                                           
        'notice_list': notice_list,         
    }
    return HttpResponse(template.render(context, request))	

def register(request):
    if request.method == 'POST':
	form = Register(request.POST)
        if form.is_valid():
	    username = form.cleaned_data['username']
       	    password = form.cleaned_data['password']
            email = form.cleaned_data['email']
       	    first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            branch = form.cleaned_data['branch']
            enr_no = form.cleaned_data['enr_no']
	    user = User(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
	    user.save()
            user_details = UserDetail(user=user,branch=branch,enr_no=enr_no)
	    user_details.save()
            login(request, user)
	    return HttpResponseRedirect(reverse('bulletin:register'))
	else:        
            return render(request, 'bulletin.html')
    else:
	form = Register(request.POST)
        return render(request, 'bulletin/register.html')
