from rest_framework import serializers
from backend.models import News, Comments, Signals, Rumors, FavoriteCoin
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "username", "password", "email"]


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class CommentsSerializer(serializers.ModelSerializer):
    user = AuthorsSerializer()

    class Meta:
        model = Comments
        fields = "__all__"


class SignalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signals
        fields = "__all__"


class RumorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rumors
        fields = ["id", "title", "content", "image"]


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ["id", "title", "content", "image", "comments"]


class FavoriteCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCoin
        fields = "__all__"
