from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#created tittle in a field of Post database
class Post(models.Model):
# Now create attributes
    tittle = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateField(default = timezone.now)
    #one user can multiple post but only one author for one post
    author = models.ForeignKey(User,on_delete=models.CASCADE)



