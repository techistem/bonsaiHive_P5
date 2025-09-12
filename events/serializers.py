from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate(self, data):
        start = data.get('start_time')
        end = data.get('end_time')
        if start and end and start >= end:
            raise serializers.ValidationError({
                'end_time': 'End time must be after start time.'
            })
        return data

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
