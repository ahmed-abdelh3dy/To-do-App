from .serializer import UserSerializer
from .models import CustomeUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError



class RegisterView(APIView):
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]

    @extend_schema(
        request=UserSerializer,  
        responses={200: UserSerializer},
    )
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if CustomeUser.objects.filter(username=username).exists():
            return Response({'error': 'username already exists'}, status=400)

        if CustomeUser.objects.filter(email=email).exists():
            return Response({'error': 'email already exists'}, status=400)

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': e.messages}, status=400)

        user = CustomeUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        serializer = UserSerializer(user)
        return Response({"user registered": serializer.data}, status=200)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        username = request.user.username
        lists = request.user.lists.all()
        count = 0
        for list in lists:
            tasks = list.tasks.count()
            count += tasks

        return Response({"username is  ": username, "total tasks": count})
