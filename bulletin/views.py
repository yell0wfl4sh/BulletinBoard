from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login
from forms import Login
from django.urls import reverse
from django.template import loader
from django.shortcuts import render


def index(request):
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
		return HttpResponseRedirect("Input Invalid")
    else:
	form = Login()
    return render(request, 'bulletin/index.html',{'form':form,})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('bulletin:index'))

def notice(request):
    latest_notice_list = Notice.objects.order_by('-upload')
    template = loader.get_template('bulletin/notices.html')
    context = {
        'latest_notice_list': latest_notice_list,
    }
    return HttpResponse(template.render(context, request))

def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'bulletin/notice_detail.html', {'notice': notice}) 

def student(request):
     student_list = Student.objects.all().order_by('enr_no')
     template = loader.get_template('bulletin/students.html')
     context = {                                           
         'student_list': student_list,         
     }
     return HttpResponse(template.render(context, request))

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'bulletin/student_detail.html', {'student': student}) 

def category(request):
    category_list = Category.objects.all().order_by('name')
    template = loader.get_template('bulletin/categories.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))    

def category_notice(request,category_id):
    category = get_object_or_404(Category, pk=category_id)
    notice_list = Notice.objects.all().filter(category = category_id)
    template = loader.get_template('bulletin/category_notice.html')
    context = {                                           
        'notice_list': notice_list,         
    }
    return HttpResponse(template.render(context, request))

def change_password(request):
    template_response = views.password_change(request)
    # Do something with `template_response`
    return template_response
