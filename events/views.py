from rest_framework import generics, filters
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from bonsaiHive_P5.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_time', 'end_time', 'created_at', 'title']
    ordering = ['start_time']

    def get_queryset(self):
        return Event.objects.filter(is_approved=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Event.objects.all()
