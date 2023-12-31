from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from backend.models import News, Comments, Signals, Rumors, FavoriteCoin
from .serializers import (
    NewsSerializer,
    SignalsSerializer,
    RumorsSerializer,
    CommentsSerializer,
    FavoriteCoinSerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework import permissions


class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_id = self.request.data.get("user_id")
        user = get_object_or_404(User, pk=user_id)
        serializer.save(user=user, news=self.get_news_object())

    def get_news_object(self):
        # Implement a method to get the News object based on your requirements
        # You can extract the news ID from the URL or request data, then retrieve the corresponding News object
        # Example:
        news_id = self.kwargs.get("news_id")  # Adjust based on your URL pattern
        return News.objects.get(id=news_id)


class SignalsApiView(generics.ListCreateAPIView):
    queryset = Signals.objects.all()
    serializer_class = SignalsSerializer


class RumorsApiView(generics.ListCreateAPIView):
    queryset = Rumors.objects.all()
    serializer_class = RumorsSerializer


class FavoriteCoinCreateView(generics.ListCreateAPIView):
    model = FavoriteCoin
    queryset = FavoriteCoin.objects.all()
    serializer_class = FavoriteCoinSerializer
    # fields = ["coin_id", "name", "symbol"]


from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.response import Response


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["POST"])
def login(request):
    print("request.data", request.data)
    user = get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")


class SendOfferView(generics.RetrieveDestroyAPIView):
    def get(self, request, blog_id):
        news = News.objects.get(pk=blog_id)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
