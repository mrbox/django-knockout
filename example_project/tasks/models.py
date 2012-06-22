from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=250)
    is_done = models.BooleanField(default=False)

    def __unicode__(self):
        #noinspection PyStringFormat
        return u"%s..." % self.description[:30]