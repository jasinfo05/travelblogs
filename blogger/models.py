from django.db import models

class blog(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'pics')
    about = models.TextField()
    date = models.DateField(auto_now_add=True)

def __str__(self):
        return self.name
# Create your models here.
