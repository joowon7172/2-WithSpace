from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from django.contrib import auth


def home(request):  # 로그인 성공 시 확인하기 위한 테스트용 페이지
    return render(request, 'home.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # 해당 계정 정보가 있는지 확인
        user = authenticate(username = username, password = password)
        
        if user is not None:    # 로그인 성공
            login(request, user)
            return redirect('home')
        else:
            # 로그인 실패
            return render(request, 'login.html', {'error': '아이디와 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')


def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                # Django 기본 User 필드
                username = request.POST["username"],
                password = request.POST["password"],

                # 확장 User 필드
                nickname = request.POST["nickname"],
                phone = request.POST["phone"]
            )
            user.save()
            
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def mypage(request):
    return render(request, 'mypage.html')