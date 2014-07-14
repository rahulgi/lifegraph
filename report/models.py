from django.db import models

class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    date = models.DateTimeField()
    text = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()

    def __unicode__(self):
        return self.date + ': ' + self.rating
