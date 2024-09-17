from django.shortcuts import render,HttpResponseRedirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from . import models

# Create your views here.

def Home(request):
        return render(request,'index.html')

def UserRegistration(request):
        if request.method == 'POST':
                registration_form = forms.UserRegistrationForm(request.POST)
                if registration_form.is_valid():
                        messages.success(request,"User registration successful!")
                        registration_form.save()
        else:
                registration_form = forms.UserRegistrationForm()
        context = {
                "registration_form":registration_form
        }
        return render(request,'user-registration.html',context)

def UserLogin(request):
        if request.method=='POST':
                form = AuthenticationForm(request=request,data=request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        user = authenticate(username=username,password=password)
                        if user is not None:
                                messages.success(request,'You have been successfully loggedin')
                                login(request,user)
        else:
                form = AuthenticationForm()

        context = {
                'login_form':form
        }
        return render(request,'login.html',context)

def CreateUserProfile(request):
        if request.method == 'POST':
                form = forms.UserProfileForm(request.POST, request.FILES)
                if form.is_valid():
                        print(form.as_p)
                        messages.success(request,"Your Profile has been created successfully!")
                        form.save()
                        form = forms.UserProfileForm()
        else:
                form = forms.UserProfileForm()
        
        context = {
                'profile_form':form
        }
        return render(request,'profile/create.html',context)


def UserProfile(request,user):
        profile = models.UserProfileModel.objects.get(user=user)
        jobs_created = models.JobModel.objects.filter(created_by=user)
        jobs_applied = models.ApplyJobModel.objects.filter(user=user)
        context = {
                'profile':profile,
                'jobs_created':jobs_created,
                'jobs_applied':jobs_applied
        }
        return render(request,'profile/display.html',context)

def CreateJob(request):
        if request.method=='POST':
                form = forms.JobForm(request.POST)
                if form.is_valid():
                        messages.success(request,'Job Created Successfully !')
                        form.save()
                        form = forms.JobForm()
                        # HttpResponseRedirect('')
        else:
                form = forms.JobForm()
        context = {
                'job_form':form
        }
        return render(request,'job/create.html',context)


def GetAllJobs(request):
        jobs = models.JobModel.objects.all()
        context = {
                'jobs':jobs
        }
        return render(request,'job/all-jobs.html',context)


def JobDetails(request,job_id):
        # if job_id is not None:
        job = models.JobModel.objects.get(id=job_id)

        context = {
                'job':job
        }
        return render(request,'job/details.html',context)


def ApplyNow(request,user,job):
        if models.JobModel.objects.get(id=job) and models.UserProfileModel.objects.get(user=user):
                if request.method == 'POST':
                        form = forms.ApplyJobForm(request.POST)
                        if form.is_valid():
                                messages.success(request,"You have successfully applied !")
                                form.save()
                                form = forms.ApplyJobForm()
                else:
                        form = forms.ApplyJobForm()
        
        context = {
                'apply_form': form
        }
        return render(request,'job/apply.html',context)