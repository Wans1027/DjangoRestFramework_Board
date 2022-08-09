from rest_framework import viewsets
from .models import Post
from users.models import Profile
from .serializers import PostSerializer, PostCreateSerializer
from .permissions import CustomReadOnly
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['author', 'likes']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)