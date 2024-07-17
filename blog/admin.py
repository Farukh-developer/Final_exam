from django.contrib import admin

from .models import ( Course, Topic, VideoLesson, Comment, Rating)

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 0

class VideoLessonInline(admin.TabularInline):
    model = VideoLesson
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'created_by', 'created_at')
    list_editable = ('title',)
    inlines = [TopicInline]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('video_lesson', 'user', 'liked', 'created_at')
    list_editable = ('user', 'liked')

