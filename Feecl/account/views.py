from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    if request.method=='GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        username=request.POST.get('username', None)
        password=request.POST.get('password', None)
        re_password=request.POST.get('re_password', None)
        generation=request.POST.get('generation', None)
        student_code=request.POST.get('student_code', None)
        
        res_data={}
        if not (username and password and re_password and generation and student_code):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password!=re_password:
            res_data['error']='비밀번호가 다릅니다.'
        elif student_code != '20211022':
            res_data['error']='학생코드가 다릅니다.'
        else:
            user=User(username=username, password=password,generation=generation)
            user.save()
            return render(request,'home.html')
        return render(request, 'register.html', res_data)


def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'home.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else:
            try:  
                myuser = User.objects.get(username=login_username)
            except:
                response_data['error']='존재하지 않는 계정입니다.'
                return render(request, 'home.html',response_data)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if login_password == myuser.password:
                request.session['user'] = myuser.id
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/starRating/1')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'home.html',response_data)

def guest(request):
    request.session['user'] = 0
    return redirect('/starRating/1')