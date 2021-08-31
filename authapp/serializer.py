from django.core.exceptions import FieldDoesNotExist
from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User,Referrals
import uuid;


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','username','first_name','last_name','referred_by_code','password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.referral_code_self = uuid.uuid4().hex.upper()[0:8]
        user.save()
        if(validated_data['referred_by_code']):
            user.incentives = user.incentives+10
            user2 = User.objects.get(referral_code_self = user.referred_by_code)
            user2.incentives = user2.incentives+10
            user2.save()
            ref = Referrals.objects.create(referee = user2,referred_to = user,referee_inc = user.share, referred_to_inc = 20 - user.share)
            ref.save()
            user.save()
        return user

class getrefcode(serializers.ModelSerializer):
    referral_code_self = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','referral_code_self']
    # def validate(self, attrs):
    #     ref = attrs.get('referral_code_self')
    #     user = User.objects.get(username = attrs.get('username'))
    #     print(attrs,self)
    #     if ref == "":
    #         new_code = uuid.uuid4().hex.upper()[0:8]
    #         user.referral_code_self = new_code
    #         user.save()
    #         attrs.update({'referral_code_self': new_code})
    #     return attrs

class getusername(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class getmaskedusername(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ReferralSerializer(serializers.ModelSerializer):
    referee = serializers.EmailField()
    referred_to = serializers.EmailField()
    class Meta:
        model = Referrals
        fields = ['referee','referred_to','referee_inc','referred_to_inc']

    def validate(self, data):
        user = data.get('referee')
        user_obj = User.object.get(id = user).username
        data.update({'referee':user_obj})
        user2 = data.get('referred_to')
        masked = User.objects.get(id = user2).username
        lo = masked.find('@')
        if lo>0:
            masked = masked[0] + '*******' + masked[lo-1] + '@' + masked[lo+1] + "*****" + masked[-1]
        data.update({'referred_to': masked})
        return data
 
