#!/usr/bin/env python
from PIL import Image, ImageFilter
import PIL
import numpy 
import colorsys

'''
Keith Murray
A program which aids in visualize genomes 
http://effbot.org/imagingbook/imagedraw.htm
http://stackoverflow.com/questions/17049777/hsl-python-syntax-pil
https://en.wikipedia.org/wiki/HSL_and_HSV

https://packaging.python.org/en/latest/distributing/

inV	RGB		HSL
1	R =255-f1(i)	H = 0:f1(i):240 (range 0:360)
	G = f1(i)	S = 100
	B = 0		L = 50

2	R =255-f1(i)	H = 0:f1(i):240 (range 0:360)
	G = f1(i)	S = 100
	B = f2(i)	L = f2(i)

3	R = f1(i)	H = 0:f1(i):240 (range 0:360)
	G = f2(i)	S = f3(i)
	B = f3(i)	L = f2(i)



    myA = numpy.array(myArray)
    myA = myA * (255/float(largest))
    myA = myA.astype(int)
'''
def drawRGB(R, G, B, width, filename):
    trailing = width - len(R)%width
    # Fill out the three vectors
    if len(G) == 0:
	G = numpy.append([], R)
	B = numpy.zeros(len(R))
	for i in range(len(G)):
	    R[i] = 1.0-G[i]

    elif len(B) == 0:
	B = numpy.append([], G)
	G = numpy.append([], R)
	for i in range(len(G)):
	    R[i] = 1.0-G[i]
    

    R = numpy.append(R, numpy.zeros(trailing))
    B = numpy.append(B, numpy.zeros(trailing))
    G = numpy.append(G, numpy.zeros(trailing))

    drawImage(R, G, B, width, filename)
    
    return

'''
Keith Murray
A program which aids in visualize genomes 
http://effbot.org/imagingbook/imagedraw.htm
http://stackoverflow.com/questions/17049777/hsl-python-syntax-pil
https://en.wikipedia.org/wiki/HSL_and_HSV

https://packaging.python.org/en/latest/distributing/

inV	RGB		HSL
1	R =255-f1(i)	H = 0:f1(i):240 (range 0:360)
	G = f1(i)	S = 100
	B = 0		L = 50

2	R =255-f1(i)	H = 0:f1(i):240 (range 0:360)
	G = f1(i)	S = 100
	B = f2(i)	L = f2(i)

3	R = f1(i)	H = 0:f1(i):240 (range 0:360)
	G = f2(i)	S = f3(i)
	B = f3(i)	L = f2(i)



    myA = numpy.array(myArray)
    myA = myA * (255/float(largest))
    myA = myA.astype(int)
'''
def drawHSL(H, S, L, width, filename):
    trailing = width - len(H)%width
    if len(L) == 0:
	H = H*240.0/360.0 # Squish it so the highest H isn't close to the lowest H
	S = numpy.zeros(len(H))
	S = S + 1.0
	L = numpy.zeros(len(H))
	L = L + 0.5
    elif len(S) == 0:
	H = H*240.0/360.0 # Squish it so the highest H isn't close to the lowest H
	S = numpy.zeros(len(H))
	S = S + 1.0
	
    else:
	H = H*240.0/360.0 # Squish it so the highest H isn't close to the lowest H
	
    H = numpy.append(H, numpy.zeros(trailing))
    S = numpy.append(S, numpy.zeros(trailing))
    L = numpy.append(L, numpy.zeros(trailing))
    R = []
    G = []
    B = []

    for i in range(len(H)):
	rgb = colorsys.hls_to_rgb(H[i], L[i], S[i])
	R.append(rgb[0])
	G.append(rgb[1])
	B.append(rgb[2])

    R = numpy.array(R)
    G = numpy.array(G)
    B = numpy.array(B)

    drawImage(R, G, B, width, filename)
   
    return

def drawImage(R, G, B, width, filename):

    depth = int(len(R)/width)
    R = R.reshape((depth, width), order="C")
    G = G.reshape((depth, width), order="C")
    B = B.reshape((depth, width), order="C")

    rgb = numpy.zeros((depth, width, 3), 'uint8')
    rgb[..., 0] = R*255
    rgb[..., 1] = G*255
    rgb[..., 2] = B*255
    img = Image.fromarray(rgb, "RGB")
    img.save(filename, "PNG")
    img.show()
    return

def drawGrey(L, width, filename):
    trailing = width - len(L)%width
    L = numpy.append(L, numpy.zeros(trailing))
    depth = len(L)/width
    L = L.reshape((depth, width), order="C")
    im = numpy.zeros((depth, width), 'uint8')
    im = L*255
    # samp = numpy.zeros(100)
    # reshape((4, 25) order="C")
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    im = Image.fromarray(im).convert("L")
    im.save(filename, "PNG")
    image = Image.open(filename)
    image.show()

    return








def arrangeSequence(myArray, myWidth):
    depth = 1 + int(len(myArray)/myWidth)
    trailing = myWidth - len(myArray)%myWidth
    # Pad out the row
    for i in range(trailing):
	myArray.append(0)

    myA = myA.astype(int)

    myA = myA.reshape((myWidth, depth), order='C')

    return myA

def drawCodeTag(myA, fileName):
    #print myA
    im = Image.new('L', (len(myA[0]), len(myA)))  # type, size
    im.putdata([int(p) for row in myA for p in row])
    im.save(fileName, "PNG")
    return














