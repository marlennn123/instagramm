from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import (
    UserProfileViewSet, FollowViewSet, PostViewSet, PostLikeViewSet,
    CommentViewSet, CommentLikeViewSet, StoryViewSet, SaveViewSet, SaveItemViewSet,
    RegisterView, LogoutView, CustomLoginView
)

router = SimpleRouter()
router.register('user_profiles', UserProfileViewSet, basename='profiles')
router.register('follows', FollowViewSet)
router.register('posts', PostViewSet)
router.register('post_likes', PostLikeViewSet)
router.register('comments', CommentViewSet)
router.register('comment_likes', CommentLikeViewSet)
router.register('stories', StoryViewSet)
router.register('saves', SaveViewSet)
router.register('save_items', SaveItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

