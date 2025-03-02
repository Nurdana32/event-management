from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, SessionViewSet, AttendeeViewSet, TrackViewSet, UserViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
