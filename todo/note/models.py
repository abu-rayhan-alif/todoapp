from django.db import models

# Create your models here.

class Notes(models.Model):

    title=models.CharField(max_length=1000)
    dateTime=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    updatetime=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
