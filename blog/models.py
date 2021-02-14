from django.db import models
from django.utils import timezone


#created tittle in a field of Post database
class Post(models.Model):
# Now create attributes
    tittle = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateField(default = timezone.now)

