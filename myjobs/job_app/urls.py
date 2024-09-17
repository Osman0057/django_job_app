from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('',views.Home,name='INDEX'),
    path('user-registration',views.UserRegistration,name='REGISTRATION'),
    path('login',views.UserLogin,name='LOGIN'),
    path('profile/create',views.CreateUserProfile,name='CREATE_PROFILE'),
    path('job/create',views.CreateJob,name='CREATE_JOB'),
    path('job/<int:user>/<int:job>',views.ApplyNow,name='APPLICATION'),
    path('profile/<int:user>',views.UserProfile,name='DISPLAY_PROFILE'),
    path('jobs',views.GetAllJobs,name='ALL_JOBS'),
    path('jobs/<int:job_id>',views.JobDetails,name='JOB_DETAILS'),
     path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]