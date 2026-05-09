from rest_framework import viewsets, permissions
from .models import Like
from .serializers import LikeSerializer

class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]