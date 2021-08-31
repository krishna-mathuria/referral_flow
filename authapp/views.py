from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import User,Referrals
from .serializer import ReferralSerializer, getrefcode
import uuid 

class ReferralHistory(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReferralSerializer

    def get_queryset(self):
        return Referrals.objects.filter(referee = self.request.user)


class getRefCode(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):
        serializer = getrefcode(request.user)
        print(serializer.data['referral_code_self'])
        if serializer.data["referral_code_self"]=="" :
            new_code = uuid.uuid4().hex.upper()[0:8]
            request.user.referral_code_self = new_code
            request.user.save()
            newdict={}
            newdict.update(serializer.data)
            newdict['referral_code_self'] = new_code
            try:
                return Response(newdict, status=status.HTTP_200_OK)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)