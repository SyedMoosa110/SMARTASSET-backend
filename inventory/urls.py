from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, AssignmentViewSet, ChatHistoryViewSet
from .auth_views import register_user

router = DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'chat-history', ChatHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
]
