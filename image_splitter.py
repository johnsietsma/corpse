import Image
import os

def split(im,pieces):
    imgwidth, imgheight = im.size
    height = imgheight//pieces
    for i in range(pieces):
		box = (0, i*height, imgwidth, (i+1)*height)
		yield im.crop(box)

if __name__=='__main__':
    infile='default.jpg'
    pieces = 4
    
    im = Image.open(infile)
    for k,piece in enumerate(split(im,pieces),0):
        path="tmp/IMG-%s.png" % k
        piece.save(path)
