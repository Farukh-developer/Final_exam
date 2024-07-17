from rest_framework import serializers

from .models import (Topic, Course, Comment, VideoLesson, Rating)

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Course
        fields='__all__'


class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Topic
        fields='__all__'        
        
        
        
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=VideoLesson
        fields='__all__'
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields='__all__'  
        
class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Rating
        fields='__all__'                      
        
        
        
class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()        
        