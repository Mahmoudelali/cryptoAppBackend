
from django.shortcuts import render
# Create your views here.

from rest_framework import generics
from backend.models import News, Comments, Signals, Rumors,FavoriteCoin
from .serializers import NewsSerializer, SignalsSerializer, RumorsSerializer, CommentsSerializer,FavoriteCoinSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions

class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class SignalsApiView(generics.ListCreateAPIView):
    queryset = Signals.objects.all()
    serializer_class = SignalsSerializer

class RumorsApiView(generics.ListCreateAPIView):
    queryset = Rumors.objects.all()
    serializer_class = RumorsSerializer

class CommentsApiView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        blog = get_object_or_404(News, pk=self.kwargs['blog_id'])
        serializer.save(user=self.request.user, blog=blog)

class FavoriteCoinCreateView(generics.ListCreateAPIView):
    model = FavoriteCoin
    queryset = FavoriteCoin.objects.all()
    serializer_class = FavoriteCoinSerializer
    fields = ['coin_id', 'name', 'symbol']  # Add other fields as needed
    template_name = 'favorite_coin_form.html'


