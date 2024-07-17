from django.db import models

from django.contrib.auth.models import User

from django.core.validators import FileExtensionValidator 

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class VideoLesson(models.Model):
    topic = models.ForeignKey(Topic, related_name='video_lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='mesage/video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4','MOV', 'AVI', 'WMV'])
    ])       
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    video_lesson = models.ForeignKey(VideoLesson, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    video_lesson = models.ForeignKey(VideoLesson, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
