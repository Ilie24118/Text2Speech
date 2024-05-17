from django.db import models

from accounts.models import CustomUser

# Create your models here.
class MP3File(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    file_location = models.FileField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_location.name