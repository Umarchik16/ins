from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *
from rest_framework import routers

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet, basename='profiles')
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'posts', PostListViewSet, basename='post')
router.register(r'post-likes', PostLikeViewSet, basename='postlike')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'comment-likes', CommentLikeViewSet, basename='commentlike')
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'saved', SavedViewSet, basename='saved')
router.register(r'save-items', SaveItemViewSet, basename='saveitem')


urlpatterns = [

    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
