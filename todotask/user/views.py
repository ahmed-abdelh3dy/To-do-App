from django.shortcuts import render
from .serializer import UserSerializer
from .models import CustomeUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import UserRateThrottle
from rest_framework.throttling import AnonRateThrottle


class RegisterView(APIView):
    throttle_classes = [AnonRateThrottle]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = CustomeUser.objects.create(
            username=username, password=make_password("password")
        )

        serializer = UserSerializer(user)
        return Response({"user registerd": serializer.data}, status=200)


class LoginView(APIView):
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        password = request.data.get("password")
        username = request.data.get("username")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "user loged in",
                    "status": True,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response({"status": 404})


class ProfileView(APIView):
    def get(self, request):

        username = request.user.username
        lists = request.user.lists.all()
        count = 0
        for list in lists:
            tasks = list.tasks.count()
            count += tasks

        return Response({"username is  ": username, "total tasks": count})
