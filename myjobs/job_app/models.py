from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileModel(models.Model):
        USER_CHOICE= (("Employee","Employee"),("Employer","Employer"))
        EDUCATION= (("Intermediate","Intermediate"),("BSc","Bsc"),("BS/MSc","BS/MSc"),("MS/MPhil","MS/MPhil"))

        user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
        # profile_pic = models.ImageField(blank=True,upload_to='images/profile')
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        date_of_birth = models.DateField()
        cnic_number = models.BigIntegerField()
        user_type = models.CharField(choices=USER_CHOICE,max_length=30)
        education = models.CharField(max_length=30,choices=EDUCATION)
        resume = models.FileField(max_length=100,upload_to='pdf/resume')


class JobModel(models.Model):
        CATEGORY = (('Education','Education'),('Graphic Design','Graphic Design'),('IT and Programming','IT and Programming'),('Marketing','Marketing'),('Sales and Management','Sales and Management'))
        created_by = models.ForeignKey(User,verbose_name=(""),on_delete=models.CASCADE)
        job_title = models.CharField(max_length=120)
        job_description = models.TextField(max_length=600)
        created_on = models.DateField(auto_now_add=True)
        expire_on = models.DateField()
        is_active = models.BooleanField(default=True)
        category = models.CharField(max_length=30,choices=CATEGORY,default='Education')


class ApplyJobModel(models.Model):
        user = models.ForeignKey(User,related_name='applicants',on_delete=models.CASCADE)
        job = models.ForeignKey(JobModel,related_name='job',on_delete=models.CASCADE)


