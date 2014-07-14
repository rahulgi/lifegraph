from django.contrib.auth.models import AbstractUser
from django.db import models

class LifegraphUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
