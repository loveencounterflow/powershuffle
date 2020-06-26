#!/bin/python3
import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('-n')
args = parser.parse_args()

filename = args.file
filesizeBytes = os.path.getsize(filename)
#print(filesizeBytes)

# you can find this with: sudo blockdev --getbsz $(df --output=source $(pwd) | grep '/')
blockSize = 4096               # Bytes
bitsInBlock = blockSize * 8    # Bits

import random
f = open(filename, "rt")
count = 0
sizeRead =0
while (count < 10000):
  buffer = f.read(bitsInBlock)
  if not buffer: break
  count += buffer.count('\n')
  sizeRead += bitsInBlock
f.close()

bitsPerLine = sizeRead/count
#print(bitsPerLine)

totalLinesEst = filesizeBytes / bitsPerLine
#print("Estimated lines in file: " + str(totalLinesEst))

fh = open(filename)
for i in range(int(args.n)):
    readstart = int(random.randint(0, int(totalLinesEst)) - bitsPerLine)
    if readstart < bitsPerLine:
        readstart = 0
    else:
        fh.seek(readstart)
    scratch = fh.readline()
    print(fh.readline(), end='', flush=True)
fh.close()
