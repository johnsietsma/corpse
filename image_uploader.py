import sys
from io import BytesIO

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

import Image

from image_splitter import split

left_margin = 450
resize_width = 350


#url = 'http://corpse.tallgames.net/create/'
url = 'http://localhost:8000/create/'

# Register the streaming http handlers with urllib2
register_openers()

def upload_image(filename):
	print 'Splitting',filename
	
	im = Image.open(filename)
	
	#-----------------------
	# chop off the edge of the holder
	imgwidth, imgheight = im.size
	box = (left_margin, 0, imgwidth, imgheight)
	im = im.crop(box)
	
	#-----------------------
	# resize
	ratio = resize_width/float(im.size[0])	
	size = (resize_width,int(im.size[1]*ratio))
	print "Size",size,"ratio:",ratio
	im = im.resize(size)
	
	#-----------------------
	# Split the image
	head,torso,legs,feet = split(im,4)
	
	head.save('head.png')
	torso.save('torso.png')
	legs.save('legs.png')
	feet.save('feet.png')

	head_torso_link = raw_input('head torso link: ');
	torso_legs_link = raw_input('torso legs link: ');
	legs_feet_link = raw_input('legs feet link: ');

		
	form_data = {
	'name': 'test3',
	'head': open('head.png', 'rb'),
	'torso': open('torso.png', 'rb'),
	'legs': open('legs.png', 'rb'),
	'feet': open('feet.png', 'rb'),
	'head_torso_link': head_torso_link,
	'torso_legs_link': torso_legs_link,
	'legs_feet_link': legs_feet_link,
	}
	
	datagen, headers = multipart_encode(form_data)
	
	request = urllib2.Request(url, datagen, headers)
	print urllib2.urlopen(request).read()

if __name__=='__main__':
	filename = sys.argv[1]
	upload_image(filename)	
