from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Account
from rest_framework.decorators import api_view
from todoList_server.settings import SECRET_KEY
import bcrypt
import jwt

# Create your views here.


@api_view(['GET', 'POST'])
def signUp(request):
    if request.method == "POST":
        data = request.data
        try:
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "user already exists"}, status=200)

                # 비밀번호 암호화
                password = data['password'].encode(
                    'utf-8')  # 입력된 패스워드 바이트로 인코딩
                password_crypt = bcrpty.hashpw(
                    password, bcrpty.gensalt())  # 암호화된 비밀번호 생성
                password_crypt = password_crypt.decode(
                    'utf-8')  # DB에 저장할 수 있는 유니코드 문자열 형태로 디코딩
                Account(
                    email=data['email'],
                    password=password_crypt

                ).save()
            return JsonResponse({"message": "making a user"}, status=200)
        except KeyError:
            return JsonResponse({"message": "Invalid"}, status=400)


@api_view(['GET', 'POST'])
def signIn(request):
    if request.method == "POST":
        data = request.data
        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])

                # 비밀번호 확인.
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode(
                        {'email': data['email']}, SECRET_KEY, algorithm="HS256")
                    token = token.decode('utf-8')
                    return JsonResponse({"token": token}, status=200)
                else:
                    return JsonResponse({"message": "Invalid password"}, status=401)
            return JsonResponse({"message": "no user exists"}, status=400)
        except KeyError:
            return JsonResponse({"message": "Invalid"}, status=400)


@api_view(['POST'])
def tokenCheck(request):
    data = request.data
    user_token_info = jwt.decode(data['token'], SECRET_KEY, algorithms='HS256')
    if Account.objects.filter(email=user_token_info['email']).exists():
        return JsonResponse({"message": "success"}, status=200)

    return JsonResponse({"message": "fail"}, status=403)
