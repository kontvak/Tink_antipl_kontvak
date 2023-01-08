import argparse
import os
from process import cleaner
from algoritm2 import rast2


def getpath(filename):
    a = os.path.abspath('compare.py')
    return (a[:len(a) - 11] + '\\plagiat\\' + filename).replace( '/', '\\')


parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str, help='Input file')
parser.add_argument('outfile', type=str, help='Output file')
args = parser.parse_args()

inputfile = open(args.infile,'r')
intext = inputfile.readlines()
inputfile.close()
outputfile = open(args.outfile, 'w')


for line in intext:
    if not line.isspace():
        a, b = line.split()

        file1 = open(getpath(a), 'r')
        file2 = open(getpath(b), 'r')
        tex1 = file1.read()
        tex2 = file2.read()

        tex1 = cleaner(tex1)   #убираем коментарии
        tex2 = cleaner(tex2)
        tex1 = tex1.replace(' ', '')
        tex2 = tex2.replace(' ', '')
        tex1 = tex1.replace('\n', '')
        tex2 = tex2.replace('\n', '')

        plag = rast2(tex1, tex2) / max(len(tex1), len(tex2))

        outputfile.write(str(plag) + '\n')






