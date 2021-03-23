from django.conf import settings
from django.db import models


class Like(models.Model):
    post = models.ForeignKey("Post", related_name="likes", on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    deleted = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
    )
