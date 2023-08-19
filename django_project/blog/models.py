from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    # title = models.CharField(max_length=20,default = 'untitled')
    # content = models.TextField(default="anonymus")
    # date_posted = models.DateField(default= timezone.now)
    # author = models.CharField(max_length=40, default='')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title