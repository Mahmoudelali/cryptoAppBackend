from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static


urlpatterns = [
    path("news", views.NewsApiView.as_view(), name="news"),
    path("news/<int:blog_id>", views.SendOfferView.as_view(), name="news"),
    path("rumors", views.RumorsApiView.as_view(), name="rumors"),
    path("signals", views.SignalsApiView.as_view(), name="signals"),
    path(
        "favorite-coins/create/",
        views.FavoriteCoinCreateView.as_view(),
        name="create-favorite-coin",
    ),
    path("comments/", views.CommentCreateView.as_view(), name="comment-create"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
