from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
        list_display = ['first_name','last_name','date_of_birth','cnic_number','user_type','education','resume']


@admin.register(models.JobModel)
class JobAdmin(admin.ModelAdmin):
        list_display = ['created_by','job_title','job_description','created_on','expire_on','is_active']


@admin.register(models.ApplyJobModel)
class ApplyJobAdmin(admin.ModelAdmin):
        list_display = ['user','job']