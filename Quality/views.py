from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import Userserirializer,LoginSerializer,UserprofileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

#generate manually generate
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Userregister(APIView):
    
    def post(self,request,format=None):
        serializer=Userserirializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token ,'msg':'register sucessfull'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request,format=None):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"token":token,'msg':'login successful'},status=status.HTTP_200_OK)  
            else:
                return Response({'msg':'field_error'})

class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserprofileSerializer(instance=request.user)  # Use instance instead of data
        return Response(serializer.data, status=status.HTTP_200_OK)

        

        

                