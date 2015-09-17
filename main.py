#!/usr/bin/env python

import numpy 
import argparse, textwrap


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
    args.add_argument('-i', '--input-file', default= "sampBC.txt", help='Input file')
    args.add_argument('-d', '--dimensions', default= 1, help='Number of Vectors used in input file, or input files given')
    args.add_argument('-o', '--output-file', default= "output.png", help='Output Image Filename')
    args.add_argument('-n', '--normalize', default= True, help='Set Minimum Value of the Input to Zero')
    args.add_argument('-c', '--colorMap', default= "rbg", help='Use "RGB", "HSL", or G:Greyscale Colormap')
    args.add_argument('-d', '--dimensions', default= 1, help='Number of Vectors used in input file')
    args.add_argument('-s', '--shape', default= "s", help='Shape of image, "S"Square, "R"Rectangle')
    args.add_argument('-r', '--rectangle', default= 512, help='If shape is "Rectangle", -r defines the restricted dimension pixel count')


    args = args.parse_args()
    return args




def parseIn(infile):




def main(args):
    
