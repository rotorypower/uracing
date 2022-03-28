from django.db import models


class FotoContent(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
