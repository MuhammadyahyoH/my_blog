from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']