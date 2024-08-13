from django.db import models

# Create your models here.
class User(models.Model):
    """Model for users"""
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=24, default='')

    def __str__(self):
        """String representation of the user"""
        return self.name