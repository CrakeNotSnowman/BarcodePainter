#!/usr/bin/env python

import numpy, math
import argparse, textwrap
import os, os.path, sys

import paintBarcode


'''
Keith Murray
A program which aids in visualize genomes 
http://effbot.org/imagingbook/imagedraw.htm
http://stackoverflow.com/questions/17049777/hsl-python-syntax-pil
https://en.wikipedia.org/wiki/HSL_and_HSV
inV	RGB		HSL
1	R =255-f(i)	H = 0:f(i):240 (range 0:360)
	G = f(i)	S = 100
	B = 0		L = 50

2	R =255-f(i)	H = 0:f(i):240 (range 0:360)
	G = f(i)	S = 100
	B = f(i)	L = f(i)

3	R = f(i)	H = 0:f(i):240 (range 0:360)
	G = f(i)	S = f(i)
	B = f(i)	L = f(i)



'''


def interface():
    args = argparse.ArgumentParser(
        prog='main.py', 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='A tool set used to help visualize structures on genetic sequences',
        epilog=textwrap.dedent('''\
		Put "Help" here
		'''))
    args.add_argument('-i', '--input-file', help='Input File')
    args.add_argument('-i2', '--input-file2', help='Input File 2')
    args.add_argument('-i3', '--input-file3', help='Input File 3')
    args.add_argument('-o', '--output-file', default= "output.png", help='Output Image Filename')
    #args.add_argument('-n', '--normalize', default= True, help='[yes/no]   \t Set Minimum Value of the Input to Zero')
    args.add_argument('-c', '--colorMap', default= "HSL", help='[RGB/HSL/G]\tUse "RGB", "HSL", or "G"Greyscale Colormap')
    args.add_argument('-s', '--shape', default= "s", help='[S/R]      \tShape of image, "S"Square, "R"Rectangle')
    args.add_argument('-r', '--rectangle', type=int, default= 512, help='[int]      \tIf shape is "Rectangle", -r defines the restricted dimension pixel count')
    #args.add_argument('-w', '--warnings', default=False, help='[yes/no]   \tDisplay Warnings')


    args = args.parse_args()
    return args

def sanitize(args):
    positive = ["yes", "y", True, 1]
    negative = ["no", "n", False, 0]
    twoD = False
    # Input files
    if args.input_file != None:
	if not os.path.isfile(args.input_file):
	    raise OSError("ERROR:\t bad filepath provided for -i")
    if args.input_file2 != None:
	if not os.path.isfile(args.input_file2):
	    raise OSError("ERROR:\t bad filepath provided for -i2")
	twoD = True
    if args.input_file3 != None:
	if not os.path.isfile(args.input_file3):
	    raise OSError("ERROR:\t bad filepath provided for -i3")
	twoD = True
    # Output file
    if args.output_file == "output.png":
	import datetime, time
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')
	args.output_file = "output" + str(st) + ".png"
    if os.path.isfile(args.output_file):
	print args.output_file, " already exists, would you like to continue? [Y/N]"
	print "\t\t(Pressing enter will be treated as 'yes')"
	while True:
	    response = raw_input()
	    if response.lower() in positive:
		break
	    if response  == "":
		break
	    if response.lower() in negative:
		print "Exiting Now"
		sys.exit()
    # Normalize
    '''
    if args.normalize != True:
	if args.normalize.lower() in positive:
	    args.normalize = True
	elif args.normalize.lower() in negative:
	    args.normalize = False
	else:
	    print "Would you like the input vectors to be normalized? [Y/N]"
	    print "\t\t(Pressing enter will be treated as 'yes')"
	    while True:
	        response = raw_input()
	        if response.lower() in positive:
		    args.normalize = True
		    break
	        if response  == "":
		    args.normalize = True
		    break
	        if response.lower() in negative:
		    args.normalize = False
		    break
    '''
    # Color Map
    if twoD == True:
	if args.colorMap.upper() not in ["RGB", "HSL", "R", "H"]:
	    print "What kind of colormap would you like to use? [RGB/HSL]"
	    print "\t\t(Pressing enter will be treated as 'RGB')"
	    while True:
	        response = raw_input()
	        if response.upper() in ["RGB", "R"]:
		    args.colorMap = "RGB"
		    break
	        if response  == "":
		    args.colorMap = "RGB"
		    break
	        if response.upper() in ["HSL", "H"]:
		    args.colorMap = "HSL"
		    break
	elif args.colorMap.upper() in ["RGB", "R"]:
	    args.colorMap = "RGB"
	else:
	    args.colorMap = "HSL"
	
    else:
	# Note that greyscale makes no sense if two or more dimensions are used
	#  Therefore it is not actually an option in the previous case
	if args.colorMap.upper() not in ["RGB", "HSL", "R", "H", "G", "HLS"]:
	    print "What kind of colormap would you like to use? [RGB/HSL/G]"
	    print "\t\t(Pressing enter will be treated as 'RGB')"
	    while True:
	        response = raw_input()
	        if response.upper() in ["RGB", "R"]:
		    args.colorMap = "RGB"
		    break
	        if response  == "":
		    args.colorMap = "RGB"
		    break
	        if response.upper() in ["HSL", "H"]:
		    args.colorMap = "HSL"
		    break
	        if response.upper() == "G":
		    args.colorMap = "G"
		    break
	elif args.colorMap.upper() in ["RGB", "R"]:
	    args.colorMap = "RGB"
	elif args.colorMap.upper() == "G":
	    args.colorMap = "G"
	else:
	    args.colorMap = "HSL"

    # Shape
    if args.shape.lower() in ["square", "s"]:
	args.shape = 's'
    elif args.shape.lower() in ["rectangle", "rect", "r"]:
	args.shape = 'r'
    else:
	while True:
	    print "What kind of shape should the output image be? [Square/Rectangle]"
	    print "\t\t(Pressing enter will be treated as 'Square')"
	    response = raw_input()
	    if response.lower() in ["square", "s"]:
		args.shape = 's'
		break
	    elif response == "":
		args.shape = 's'
		break
	    elif response.lower() in ["rectangle", "rect", "r"]:
		args.shape = 'r'
		break

    # Rectangle constrained Dimension
    if args.rectangle == 'r':
	if args.rectangle < 1:
	    print "WARNING:\t Provided pixel count was too small, using default 512 instead"
	    args.rectangle = 512

		
    return args


def parseIn(infile):
    inf = open(infile, 'r')
    temp = ""
    for line in inf:
	holder = line.strip()
	if len(holder) > 0:
	    print holder[0:100]
	    if holder[0] != ">" and holder[0] != "#":
		temp = temp + holder
    temp = temp.strip()
    temp = temp.replace("\n", " ")
    temp = temp.replace("\t", " ")
    temp = temp.replace(",", " ")
    temp = temp.replace(":", " ")
    temp = temp.replace("[", " ")
    temp = temp.replace("]", " ")
    temp = temp.replace("(", " ")
    temp = temp.replace(")", " ")
    temp = temp.split(" ")
    cleanV = []
    for i in range(len(temp)):
	if temp[i] != "":
	    cleanV.append(float(temp[i]))

   
    return cleanV
def normalize(vect):
    maxSize = max(vect)	
    for i in range(len(vect)):
	if maxSize != 0:
	    vect[i] = vect[i]/float(maxSize)
	else:
	    print "WARNING:\tIt looks like you have a zero vector in the inputs"
	    vect[i] = 0.0
    return vect

def normalizeDC(vect):
    minSize = min(vect)
    for i in range(len(vect)):
	vect[i] = vect[i] - minSize
    return vect


def main(args):
    infile1 = args.input_file
    infile2 = args.input_file2
    infile3 = args.input_file3
    infCount = 1 #easy way to check if there are multiple inputs

    # Parse the input files
    if infile1 == None:
	print("WARNING:\tNo input file provided, using default instead")
	infile1 = "sampBC.txt"
    vect1 = parseIn(infile1)
    if infile2 != None:
	vect2 = parseIn(infile2)
	infCount += 1
	if len(vect1) != len(vect2):
	    raise ValueError("Vector lengths are not equal")
    else:
	vect2 = []
    if infile3 != None:
	vect3 = parseIn(infile3)
	infCount += 1
	if len(vect1) != len(vect3):
	    raise ValueError("Vector lengths are not equal")
    else:
	vect3 = []
	


    # Normalize the vectors for the colormaps
    #if args.normalize == True:
    vect1 = normalizeDC(vect1)
    vect1 = numpy.array(normalize(vect1))
    if len(vect2)>0:
	if args.normalize == True:
	    vect2 = normalizeDC(vect2)
	vect2 = numpy.array(normalize(vect2))

    if len(vect3)>0:
	if args.normalize == True:
	    vect3 = normalizeDC(vect3)
	vect3 = numpy.array(normalize(vect3))
	
    # Calculate the width
    if args.shape == 's':
	width = int(math.sqrt(len(vect1))) + 1
    else:
	width = int(args.rectangle)


    # Ok, time to rock this!
    print "Rocking in three, two, one..."
    if args.colorMap == "RGB":
	paintBarcode.drawRGB(vect1, vect2, vect3, width, args.output_file)
    elif args.colorMap == "HSL":
	# HSL is more intuitive having L be the second provided vector,
	#  not the third
	paintBarcode.drawHSL(vect1, vect3, vect2, width, args.output_file)
    else:
	paintBarcode.drawGrey(vect1, width, args.output_file)
    '''
    import random
    alpha = [random.randint(0,3) for r in xrange(100000)]
    #beta = numpy.array(alpha) / 100000.
    delta = [r for r in xrange(100000)]
    temp = open("alpha", 'w')
    temp.write(str(alpha))
    temp.close()
    #temp = open("beta", 'w')
    #temp.write(str(beta))
    #temp.close()
    temp = open("delta", 'w')
    temp.write(str(delta))
    temp.close()
    '''
    return








args = interface()
args = sanitize(args)
main(args)
    
