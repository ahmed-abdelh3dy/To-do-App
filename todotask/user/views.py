from .serializer import UserSerializer
from .models import CustomeUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.throttling import AnonRateThrottle
from drf_spectacular.utils import extend_schema


class RegisterView(APIView ):
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]

    @extend_schema(
        request=UserSerializer,  
        responses={200: UserSerializer},
    )

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = CustomeUser.objects.create(
            username=username,
        password=make_password(password)
        )

        serializer = UserSerializer(user)
        return Response({"user registered": serializer.data}, status=200)


class ProfileView(APIView):
    def get(self, request):

        username = request.user.username
        lists = request.user.lists.all()
        count = 0
        for list in lists:
            tasks = list.tasks.count()
            count += tasks

        return Response({"username is  ": username, "total tasks": count})
