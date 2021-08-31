
from django.urls import path,include
from .views import * 


urlpatterns = [
    path('referralhistory', ReferralHistory.as_view(),name="referral_history"),
    path('mycode',getRefCode.as_view(),name="get_referral_code"),
]