from rest_framework import serializers
from .models import Event, Session, Attendee, Track
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(source='event', queryset=Event.objects.all(), write_only=True)
    track_id = serializers.PrimaryKeyRelatedField(source='track', queryset=Track.objects.all(), write_only=True)

    event = serializers.IntegerField(source='event.id', read_only=True)
    track = serializers.IntegerField(source='track.id', read_only=True)

    class Meta:
        model = Session
        fields = ['id', 'event_id', 'event', 'title', 'description', 'start_time', 'end_time', 'speaker', 'track_id', 'track']
    def validate(self, data):
        track_id = data.get("track")
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        
        if Session.objects.filter(track=track_id,start_time__lt=end_time,end_time__gt=start_time).exists():
            raise serializers.ValidationError("This time slot overlaps with an existing session in the same track.")
        if Session.objects.filter(track=track_id,start_time=start_time,end_time=end_time).exists():
            raise serializers.ValidationError("This time slot overlaps with an existing session in the same track.")
            
        return super().validate(data)

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'
        
    def validate(self, data):
        user = data.get("user")
        event = data.get("event")

        # Cek apakah event valid
        if not event:
            raise serializers.ValidationError({"event": "Event is required."})

        # Cek apakah event sudah penuh
        attendee_count = Attendee.objects.filter(event=event).count()
        if attendee_count >= event.capacity:
            raise serializers.ValidationError({"event": "Event is full. Registration closed."})

        # Cek apakah user sudah terdaftar di event ini
        if Attendee.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError({"user": "User is already registered for this event."})

        return data