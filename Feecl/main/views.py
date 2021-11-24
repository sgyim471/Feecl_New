from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import School

# Create your views here.
def index(request):
    try:
        login_check = request.session['user']
        if login_check == 0:
            login_check = 1
        return render(request, 'main.html',{'user':login_check})
    except:
        login = 0
        return render(request, 'main.html',{'user':login})

def schoolList(request):
    try:
        school = request.GET['search']
        schoolList = School.objects.filter(school_name__icontains=school)
        try:
            login_check = request.session['user']
            if login_check == 0:
                login_check = 1
            return render(request,'main.html',{'schoolList':schoolList, 'user':login_check})
        except:
            login = 0
            return render(request,'main.html',{'schoolList':schoolList, 'user':login})
    except:
        schoolList = None
        return render(request,'main.html',{'schoolList':schoolList}) 


def logoutMain(request):
    request.session.pop('user')
    login = 0
    return render(request, 'main.html',{'user':login})
