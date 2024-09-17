from django.urls import path,include
from . import views

urlpatterns = [
    path('profile',views.UserProfile.as_view()),
    path('profile/<int:pk>',views.UserProfile.as_view()),
    path('jobs',views.Jobs.as_view()),
    path('jobs/<int:pk>',views.Jobs.as_view()),
    path('accounts',views.Accounts.as_view()),
    path('application/<int:pk>/<int:user_id>',views.ApplyToJob.as_view()),
    path('profile/<int:pk>/jobs',views.UserCreatedJobs.as_view())
]