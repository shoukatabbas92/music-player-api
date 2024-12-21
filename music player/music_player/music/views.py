from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Music
from .serializers import MusicSerializer


class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(uploaded_at=self.request.user)

class MusicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
