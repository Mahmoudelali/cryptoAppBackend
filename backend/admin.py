from django.contrib import admin
from backend import models

admin.site.register(models.Comments)
admin.site.register(models.FavoriteCoin)
admin.site.register(models.Rumors)
admin.site.register(models.News)
admin.site.register(models.Signals)