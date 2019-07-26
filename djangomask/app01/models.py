from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=18)

    password = models.CharField(max_length=128)
    def __str__(self):
        return self.username
    def __repr__(self):
        return self.username