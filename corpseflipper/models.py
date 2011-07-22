from django.db import models

class Corpse(models.Model):
	'''A set of images making up a corpse.'''
	name = models.CharField(max_length=200)
    
	head = models.ImageField(upload_to='corpse_images/heads')
	torso = models.ImageField(upload_to='corpse_images/torsos')
	legs = models.ImageField(upload_to='corpse_images/legs')
	feet = models.ImageField(upload_to='corpse_images/feet')
	
	def __unicode__(self):
		return self.name  
