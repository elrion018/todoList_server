from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def signUp(request):
    if request.method == "POST":
        data = request.body
        Account(
            email=data['email'],
            password=data['password']
        ).save()

        return JsonResponse({'message': '회원가입 완료'}, status=200)


# @csrf_exempt
# @ensure_csrf_cookie
@api_view(['GET', 'POST'])
def signIn(request):
    if request.method == "POST":
        data = request.body

        if Account.objects.filter(email=data['email']).exists():
            user = Account.objects.get(email=data['email'])
            if user.password == data['password']:
                return JsonResponse({'message': f'{user.email}님 로그인 성공!'}, status=200)
            else:
                return JsonResponse({'message': '비밀번호가 틀렸어요'}, status=200)

        return JsonResponse({'message': '등록되지 않은 이메일입니다.'}, status=200)
