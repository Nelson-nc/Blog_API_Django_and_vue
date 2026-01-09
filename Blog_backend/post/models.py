from django.db import models
from account.models import Profile


class Post(models.Model):
    image = models.ImageField(upload_to="post_image", blank=True, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(Profile, blank=True, related_name="post_likes")

    def __str__(self) -> str:
        return f"Author:{self.user_id} <==> {self.title}"
    
    def post_like(self):
        total_likes = 0
        for like in self.likes.all():
            total_likes += 1
        return total_likes
    

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile, blank=True, related_name="comment_likes")

    def __str__(self) -> str:
        return f"Author:{self.user_id} <==> {self.post_id}"

    def comment_like(self):
        total_likes = 0
        for like in self.likes.all():
            total_likes += 1
        return total_likes
