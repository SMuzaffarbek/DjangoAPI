from .serializers import PostSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework import permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
