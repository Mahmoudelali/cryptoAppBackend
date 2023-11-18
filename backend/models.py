from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/", null=True, blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey(
        News, related_name="comments", on_delete=models.CASCADE, null=True
    )
    comment_content = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class Signals(models.Model):
    signal_type = models.CharField(max_length=5, null=True, default=None)
    coin_name = models.CharField(max_length=50)
    entry_price = models.DecimalField(
        max_digits=10, decimal_places=4
    )  # Adjust max_digits as needed
    target = models.DecimalField(
        max_digits=10, decimal_places=4
    )  # Adjust max_digits as needed
    leverage = models.PositiveIntegerField()
    stop_loss = models.DecimalField(
        max_digits=10, decimal_places=4
    )  # Adjust max_digits as needed


class Rumors(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/", null=True, blank=True)


class FavoriteCoin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.symbol}) - User: {self.user.username}"
