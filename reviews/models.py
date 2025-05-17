from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from posts.models import Post 


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=
                              models.CASCADE, related_name='reviews')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner.username} {self.post.title}: {self.title}"