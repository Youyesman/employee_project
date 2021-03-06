from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as auth_logout


# Create your views here.

# 회원 가입


def signup(request):

    if request.user.is_authenticated:
        # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
        return redirect('/main')
    else:
        if request.method == 'POST':
            # password와 confirm에 입력된 값이 같다면
            if request.POST['password'] == request.POST['confirm']:
                # user 객체를 새로 생성
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password'])
                # 로그인 한다
                auth.login(request, user)

                return redirect('/users/login')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
        return render(request, 'users/signup.html')


def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/main/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'users/login.html', {'error': 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'users/login.html')

# 로그 아웃


def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'GET':
        auth_logout(request)
        return redirect('/users/login')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'users/login.html')
