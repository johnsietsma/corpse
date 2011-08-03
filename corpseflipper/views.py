from django.views.generic.simple import direct_to_template, redirect_to
from django.views.decorators.csrf import csrf_exempt

from models import Corpse, CorpseForm

def random_torso(head_torso_link):
	corpses = Corpse.objects.filter(head_torso_link=head_torso_link)
	return random_or_default( corpses, Corpse.default_torso )

def random_legs(torso_legs_link):
	corpses = Corpse.objects.filter(torso_legs_link=torso_legs_link)
	return random_or_default( corpses, Corpse.default_legs )

def random_feet(legs_feet_link):
	corpses = Corpse.objects.filter(legs_feet_link=legs_feet_link)
	return random_or_default( corpses, Corpse.default_feet )


def random_or_default( corpses, default):
	if corpses.count() > 0:
		c = corpses.order_by('?')[0].url
	else:
		c = Corpse.default_head
	return c


def random(request):
	if Corpse.objects.count() > 0:
		c = Corpse.objects.order_by('?')[0]
		head = c.head
		torso = random_torso(head.head_torso_link)
		legs = random_legs(torso.torso_legs_link)
		feet = random_torso(legs.legs_feet_link)
		extra = { 
			'head': head.url,
			'torso': torso.url,
			'legs': legs.url, 
			'feet': feet.url
		}
	else:
		extra = {
			'head': Corpse.default_head,
			'torso': Corpse.default_torso,
			'legs': Corpse.default_legs,
			'feet': Corpse.default_feet
		}
	return direct_to_template(request, 'corpseflipper/random.html', extra)

def random_head(request, link_type):
	corpses = Corpse.objects.filter(head_torso_link=link_type)
	if corpses.count() > 0:
		c = corpses.order_by('?')[0].url
	else:
		c = Corpse.default_head

	return redirect_to(request, url=c)

@csrf_exempt
def create(request):
    if request.method == 'POST':
        form = CorpseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CorpseForm()
        
    extra = { 
             'corpse': form, 
             }        
    return direct_to_template(request, 'corpseflipper/corpse.html', extra)