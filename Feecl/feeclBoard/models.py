from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Board(models.Model):
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    writer_id = models.PositiveIntegerField(default=1)
    view_count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

class Comment_Board(models.Model):
    post=models.ForeignKey('Board', on_delete=models.CASCADE, null=True, related_name='comments')
    comment_created_date=models.DateTimeField(auto_now_add=True)
    comment_contents=models.CharField(max_length=200)
    comment_writer = models.PositiveIntegerField(default=0)
    comment_writer_id = models.PositiveIntegerField(default=1)
    """ comment_author=models.ForeignKey(Post, on_delete=models.CASCADE, null=True) """

    class Meta:
        ordering=['-id']

