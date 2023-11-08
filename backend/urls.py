
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('news', views.NewsApiView.as_view(), name='news'),
    
    path('rumors', views.RumorsApiView.as_view() , name='rumors'),
    path('signals', views.SignalsApiView.as_view() , name='signals'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('news/<int:blog_id>/comment/', views.CommentsApiView.as_view(), name='comment-create'),
    path('favorite-coins/create/', views.FavoriteCoinCreateView.as_view(), name='create-favorite-coin'),
    path('admin/', admin.site.urls),
    path('accounts/', include('backend.urls')),
]
