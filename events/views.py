from rest_framework import viewsets, permissions
from .models import Event, Session, Attendee, Track
from .serializers import EventSerializer, SessionSerializer, AttendeeSerializer, TrackSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()

def handle_retrieve(viewset, request, *args, **kwargs):
    try:
        return super(viewset.__class__, viewset).retrieve(request, *args, **kwargs)
    except Http404:
        return Response({"error": f"{viewset.queryset.model.__name__} not found."}, status=status.HTTP_404_NOT_FOUND)

def handle_update(viewset, request, *args, **kwargs):
    try:
        return super(viewset.__class__, viewset).update(request, *args, **kwargs)
    except Http404:
        return Response({"error": f"{viewset.queryset.model.__name__} not found, update failed."}, status=status.HTTP_404_NOT_FOUND)

def handle_destroy(viewset, request, *args, **kwargs):
    try:
        instance = viewset.get_object()
        obj_name = instance.__str__()
        viewset.perform_destroy(instance)
        return Response({"message": f"{viewset.queryset.model.__name__} '{obj_name}' has been deleted successfully."}, status=status.HTTP_200_OK)
    except Http404:
        return Response({"error": f"{viewset.queryset.model.__name__} not found, delete failed."}, status=status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        return handle_retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return handle_destroy(self, request, *args, **kwargs)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return handle_retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return handle_destroy(self, request, *args, **kwargs)
    
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        return handle_retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return handle_destroy(self, request, *args, **kwargs)

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        return handle_retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return handle_destroy(self, request, *args, **kwargs)
    
class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        return handle_retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return handle_destroy(self, request, *args, **kwargs)

