from django.urls import path, include
from .views import VideoAPIView, CommentAPIView, CourseAPIView, TopicAPIView, RatingAPIView
from rest_framework import routers



router=routers.SimpleRouter()
router.register("video", VideoAPIView)
router.register("comment", CommentAPIView)
router.register("course", CourseAPIView)
router.register("topic", TopicAPIView)
router.register("rating", RatingAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    
    ### Djoser
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
]
