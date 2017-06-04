'''
rangeGenerator.py
Arguements: -s <size>, -r <rangeLimit>, -o <outputFile>
Author: Yi Liu
Build a set of 100 (default size) range queries
Format:
 x_1 x'_1 y_1 y'_1
 ......
 x_m x'_m y_m y'_m
 ......
'''
import sys
import getopt
import random

# define a random rectangular and write into file
def buildRectangular(fileHandle, rangeLimit):
    x1 = round(random.uniform(-rangeLimit, rangeLimit),2)
    x2 = round(random.uniform(-rangeLimit, rangeLimit),2)
    y1 = round(random.uniform(-rangeLimit, rangeLimit),2)
    y2 = round(random.uniform(-rangeLimit, rangeLimit),2)
    
    content = str(x1) + ' ' + str(x2) + ' ' + str(y1) + ' ' + str(y2)
    fileHandle.write(content + '\r\n')

def main():
    fileName = 'queriesRange.txt'
    size = 100
    rangeLimit = 500
    
    # parse arguements
    options,args = getopt.getopt(sys.argv[1:],"s:r:o:")
    for opt, para in options:
        if opt == '-s':
            size = int(para)
        if opt == '-r':
            rangeLimit = int(para)
        if opt == '-o':
            fileName = para

    f = open(fileName, 'wt')
    
    for i in range(1, size+1):
        buildRectangular(f, rangeLimit)
    
    f.close()
    print('Finished')

if __name__ == '__main__':
    main()
