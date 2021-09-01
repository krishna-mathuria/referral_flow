from django.core.exceptions import FieldDoesNotExist
from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User,Referrals
import uuid;

# Serializer user to create a new user
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
            user2 = User.objects.get(referral_code_self = user.referred_by_code)
            user2.incentives = user2.incentives+user2.share
            user.incentives = user.incentives+(20 - user2.share)
            user2.save()
            ref = Referrals.objects.create(referee = user,referred_by = user2,referred_by_inc = user2.share, referee_inc = 20 - user2.share)
            ref.save()
            user.save()
        return user

# Serializer to receive the referral code and the username of the authenticated user
class getrefcode(serializers.ModelSerializer):
    referral_code_self = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','referral_code_self']



# Serializer to get details for the referral history
class ReferralSerializer(serializers.ModelSerializer):
    referee = serializers.EmailField()
    referred_by = serializers.EmailField()
    class Meta:
        model = Referrals
        fields = ['referee','referred_by','referee_inc','referred_by_inc']


 # User details serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','referred_by_code','referral_code_self','incentives')