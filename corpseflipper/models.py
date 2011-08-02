from django.db import models
from settings import MEDIA_URL

class Corpse(models.Model):
	'''A set of images making up a corpse.'''
	name = models.CharField(max_length=200)
    
	head = models.ImageField(upload_to='corpse_images/heads')
	torso = models.ImageField(upload_to='corpse_images/torsos')
	legs = models.ImageField(upload_to='corpse_images/legs')
	feet = models.ImageField(upload_to='corpse_images/feet')
	
	head_torso_link = models.CharField(max_length='10')
	torso__legs_link = models.CharField(max_length='10')
	legs_torso_feet = models.CharField(max_length='10')
	
	default_head = '%s%s' % (MEDIA_URL,'corpse_images/heads/default.jpg')
	default_torso = '%s%s' % (MEDIA_URL,'corpse_images/torsos/default.jpg')
	default_legs = '%s%s' % (MEDIA_URL,'corpse_images/legs/default.jpg')
	default_feet = '%s%s' % (MEDIA_URL,'corpse_images/feet/default.jpg')
	
	def __unicode__(self):
		return self.name  
