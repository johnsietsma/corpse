from django.views.generic.simple import direct_to_template
from models import Corpse

def random(request):
	c = Corpse.objects.order_by('?')[0]
	extra = { 
		'head': c.head,
		'torso': c.torso,
		'legs': c.legs, 
		'feet': c.feet
	}
	return direct_to_template(request, 'corpseflipper/random.html', extra)
