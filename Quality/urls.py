from django.urls import path
from .views import Userregister,LoginView,UserProfileView


urlpatterns = [
    path('register/',Userregister.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('userprofile/',UserProfileView.as_view(),name='userprofile')

    
]

