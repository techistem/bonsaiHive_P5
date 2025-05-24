from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'start_time',
            'end_time',
            'location',
            'created_at',
            'owner',
            'is_approved',
        ]
        read_only_fields = ['owner', 'is_approved']
