from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user      =     models.ForeignKey(User,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
    country   =     models.CharField(max_length=100)
    state     =     models.CharField(max_length=100)
    district  =     models.CharField(max_length=100)
    city      =     models.CharField(max_length=100)
    age       =     models.CharField(max_length=100)
    profession=     models.CharField(max_length=100)
    latitude  =     models.CharField(max_length=100)
    longitude =     models.CharField(max_length=100)
    language  =     models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user}"

