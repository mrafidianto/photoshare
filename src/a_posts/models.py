from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created_at']