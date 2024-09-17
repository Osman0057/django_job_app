from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser
from rest_framework import status
from . import serializers
from job_app import models

# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['namername'] = user.username
        token['email'] = user.email
        # ...

        return token
    


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserProfile(APIView):

        parser_classes = (MultiPartParser,)
        def post(self,request,format=None):
                serializer = serializers.ProfileSerializer(data=request.POST)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data,{'message':'Your profile has been created successfully !'})


        def get(self,request,format=None):
                profile = models.UserProfileModel.objects.all()
                serializer = serializers.ProfileSerializer(profile,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
        

        def get(self,request,pk=None,format=None):
                if pk is not None:
                        profile = models.UserProfileModel.objects.get(user=pk)
                        serializer = serializers.ProfileSerializer(profile)
                        return Response(serializer.data,status=status.HTTP_200_OK)
                
        
        # def get(self,request,pk,format=None):
        #         if pk is not None:
        #                 jobs = models.JobModel.objects.get(user=pk)
        #                 serializer = serializers.JobSerializer(jobs,many=True)
        #                 return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        def put(self,request,pk=None,format=None):
                if pk is not None:
                        profile = models.UserProfileModel.objects.get(user=pk)
                        serializer = serializers.ProfileSerializer(profile,data=request.data,partial=True)
                        if serializer.is_valid():
                                serializer.save()
                                return Response(serializer.data,status=status.HTTP_200_OK)
                        else:
                                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
                        
                        
        def delete(self,request,pk,format=None):
                if pk is not None:
                        profile = models.UserProfileModel.objects.get(user=pk)
                        profile.delete()
                        return Response({'message':'Your Profile has been deleted successfully !'},status=status.HTTP_204_NO_CONTENT)
                

class Jobs(APIView):

        parser_classes = (JSONParser,)
        def get(self,request,format=None):
                jobs = models.JobModel.objects.all()
                serializer = serializers.JobSerializer(jobs,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
        

        def post(self,request,format=None):
                serializer = serializers.JobSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response({'message':'Congrations! You have successfully created a job'})



        def get(self,request,pk=None,format=None):
                if pk is not None:
                        job = models.JobModel.objects.get(id=pk)
                        serializer = serializers.JobSerializer(job)
                        return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                        jobs = models.JobModel.objects.all()
                        serializer = serializers.JobSerializer(jobs,many=True)
                        return Response(serializer.data,status=status.HTTP_200_OK)
                
                
        def put(self,request,pk=None,format=None):
                if pk is not None:
                        job = models.JobModel.objects.get(id=pk)
                        serializer = serializers.JobSerializer(instance=job,data=request.data,partial=True)
                        if serializer.is_valid():
                                serializer.save()
                                return Response(serializer.data,status=status.HTTP_200_OK)
                        else:
                                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                        

        def delete(self,request,pk=None,format=None):
                if pk is not None:
                        job = models.JobModel.objects.get(id=pk)
                        job.delete()
                        return Response({'message':'Job deleted successfully!'},status=status.HTTP_204_NO_CONTENT)
                

class Accounts(APIView):

        def get(self,request,format=None):
                users = models.User.objects.all()
                serializer = serializers.UserSerializer(users,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
        

        def post(self,request,format=None):
                serializer = serializers.UserSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response({'message':'User created successfully!'},status=status.HTTP_201_CREATED)
                

class ApplyToJob(APIView):
        def get(self,request,pk,user_id,format=None):
                job = models.JobModel.objects.get(id=pk)
                user = models.UserProfileModel.objects.get(user=user_id)
                serializer = serializers.ApplicationSerializer({'job':job,'user':user})
                return Response(serializer.data,status=status.HTTP_200_OK)
        def post(self,request,pk,user_id,format=None):
                if pk is not None and user_id is not None:
                        serializer = serializers.ApplicationSerializer(data=request.data)
                        profile = models.UserProfileModel.objects.get(user=user_id)
                        print(profile.user)
                        print(request.data['user'],request.data['job'])
                        if serializer.is_valid():
                                serializer.save()
                                return Response({'message':'User Applied Successfully!'})
                
class UserCreatedJobs(APIView):
        def get(self,request,pk,format=None):
                if pk is not None:
                        jobs = models.JobModel.objects.filter(created_by=pk)
                        serializer = serializers.JobSerializer(jobs,many=True)
                        return Response(serializer.data,status=status.HTTP_200_OK)