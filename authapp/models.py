from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class User(AbstractUser):
    username = models.EmailField(verbose_name='email', max_length=255,unique=True)
    incentives = models.IntegerField(default=0)
    referral_code_self = models.CharField(verbose_name="My Referral Code",max_length=8,unique=True,blank = True)
    referred_by_code = models.CharField(verbose_name='referral code',max_length=8,blank=True, null=True)
    REQUIRED_FIELDS = ['first_name','last_name','share']
    USERNAME_FIELD = 'username'
    share = models.IntegerField(default=10, validators=[MaxValueValidator(20), MinValueValidator(0)])
    def __str__(self):
        return self.username


class Referrals(models.Model):
    referee  = models.ForeignKey(User,related_name="referee", on_delete=models.CASCADE)
    referred_to = models.ForeignKey(User,related_name="referred_to", on_delete=models.CASCADE)
    referee_inc  = models.IntegerField(default=10)
    referred_to_inc = models.IntegerField(default=10)

    def __str__(self):
        return self.referee.username + " referred " + self.referred_to


