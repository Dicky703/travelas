from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
	#car_id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length = 128, unique = True)

	def __unicode__(self):
		return self.management

class Page(models.Model):
	car = models.ForeignKey('Car', on_delete = models.CASCADE,)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	views = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.title


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.PROTECT)

    
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

     
    def __unicode__(self):
        return self.user.username



