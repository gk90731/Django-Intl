from django.shortcuts import render
import django.conf as conf
# Create your views here.
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from .serializers import UserSerializer,UserLangSerializer
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser 
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def langConvert(request):
    if request.method == 'GET':

        # implementing translator
        output = _("Welcome to my site.")

        # changing the language code in settings.py file dynamically
        translation.activate(UserProfile.objects.filter(user=request.user)[0].language)
        request.LANGUAGE_CODE = translation.get_language()
        return Response({"output":output})
    
    if request.method == 'POST':
        serializer = UserLangSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            # if the interested item exists take the count of it and increase count number by one
            if UserProfile.objects.all().filter(user=user).exists():
                existing_UserProfile = UserProfile.objects.all().filter(user=user)
                existing_UserProfile_object = UserProfile.objects.get(user=user)
                existing_UserProfile_object.language = request.data["language"]
                existing_UserProfile_object.save()
                # implementing translator
                output = _("Welcome to my site.")

                # changing the language code in settings.py file dynamically
                translation.activate(UserProfile.objects.filter(user=request.user)[0].language)
                request.LANGUAGE_CODE = translation.get_language()
                return Response({"output":output})
            else:
                User_Serializer = UserSerializer(data=request.data)
                if User_Serializer.is_valid():
                    User_Serializer.save(user=request.user)
                    return Response(User_Serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print('error', User_Serializer.errors)
                    return Response(User_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 





  