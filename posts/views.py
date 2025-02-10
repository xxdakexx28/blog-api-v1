from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly #New 

# Create your views here.
class PostList(generics.ListCreateAPIView): 
    permission_classes = (IsAuthorOrReadOnly,) #New
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# posts detail views
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,) #New
