import os
import glob
import shutil
from image_uploader import *

inpath = 'in/'
outpath= 'out/'
for infile in glob.glob( os.path.join(inpath, '*.png') ):
	print "current file is: " + infile
	upload_image(infile)
	shutil.move(infile, outpath)
