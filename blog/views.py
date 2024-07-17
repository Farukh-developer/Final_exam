from django.shortcuts import render
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import APIView
from .models import (Topic, Course, Comment, VideoLesson, Rating)
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework import settings
from .serializers import (TopicSerializer, CourseSerializer, CommentSerializer, RatingSerializer, VideoSerializer, EmailSerializer)

class TopicAPIView(ModelViewSet):
    queryset=Topic.objects.all()
    serializer_class=TopicSerializer
    permission_classes=[]

class CourseAPIView(ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=[]

class CommentAPIView(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[]

class RatingAPIView(ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
    permission_classes=[]

class VideoAPIView(ModelViewSet):
    queryset=VideoLesson.objects.all()
    serializer_class=VideoSerializer
    permission_classes=[]




class SendEmailToUserView(APIView):
    def post(self, request: Request):   
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   

        users = User.objects.all()
        user_email = []
        for user in users:
            user_email.append(user.email)
        user_email.append("Tukhtamishev@gmail.com")

        send_mail(
            serializer.validated_data.get("sabject"),
            serializer.validated_data.get("message"),
            settings.EMAIL_HOST_USER,
            user_email,
            fail_silently=False,
        )
        return Response({"message":"Xabar yuborildi."})