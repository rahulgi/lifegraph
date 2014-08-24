from django.db import models

class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    user = models.ForeignKey('lifegraph.LifegraphUser', blank=True, null=True)

    def __unicode__(self):
        return str(self.date) + ': ' + str(self.rating)
