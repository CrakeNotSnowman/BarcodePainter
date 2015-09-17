#!/usr/bin/env python
from PIL import Image, ImageFilter
import PIL
import numpy 


def arrangeSequence(myArray, myWidth):
    depth = 1 + int(len(myArray)/myWidth)
    trailing = myWidth - len(myArray)%myWidth
    for i in range(trailing):
	myArray.append(0)
 
    largest = max(myArray)
    #print "\thigestFreq: ",largest
    if (largest == 0):
	largest = 1


    myA = numpy.array(myArray)
    myA = myA * (255/float(largest))
    myA = myA.astype(int)

    myA = myA.reshape((myWidth, depth), order='F')

    return myA

def drawCodeTag(myA, fileName):
    #print myA
    im = Image.new('L', (len(myA[0]), len(myA)))  # type, size
    im.putdata([int(p) for row in myA for p in row])
    im.save(fileName, "PNG")
    return














