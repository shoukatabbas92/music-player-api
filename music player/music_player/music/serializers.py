from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id','title','artist','file','uploaded_at','updated_at']
        read_only_fields = ['uploaded_at','updated_at']
        