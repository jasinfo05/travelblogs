from django.db import models
from blogger.models import blog

class comment(models.Model):
    blogging=models.ForeignKey(blog,related_name="comments",on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Message=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)

