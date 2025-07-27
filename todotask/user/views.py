from .serializer import UserSerializer
from .models import CustomeUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegisterView(APIView):
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]

    @extend_schema(request=UserSerializer, responses={200: UserSerializer})
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        password=serializer.validated_data["password"]

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': e.messages}, status=400)

        
        user = CustomeUser.objects.create_user(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            password=password
        )

        return Response(
            {"User Registered": UserSerializer(user).data}, status=status.HTTP_200_OK
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):

        username = request.user.username
        lists = request.user.lists.all()
        count = 0
        for list in lists:
            tasks = list.tasks.count()
            count += tasks

        return Response({"Username is  ": username, "Total Tasks": count})
