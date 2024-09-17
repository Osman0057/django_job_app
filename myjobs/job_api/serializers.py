from rest_framework import serializers
from django.contrib.auth.models import User
from job_app import models
from rest_framework.validators import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.UserProfileModel
                fields = '__all__'
        # def validate(self,validate):

class JobSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.JobModel
                fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
        # password2 = serializers.CharField(min_length=8)
        class Meta:
                model = User
                fields = ['username','email','password']

        # def validate(self, attrs):
        #         password = attrs.get('password')
        #         password2 = attrs.get('password2')
        #         if password!= password2:
        #                 raise ValidationError('Password and confirm password must be same')
        #         else:
        #                 return attrs

class ApplicationSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.ApplyJobModel
                fields = '__all__'