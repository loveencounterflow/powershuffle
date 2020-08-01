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

import random
f = open(filename, "rt")
count = 0
bytesRead = 0
while (count < 10000):
  buffer = f.read(blockSize)
  if not buffer: break
  count += buffer.count('\n')
  bytesRead += blockSize
f.close()

# less then 1 blocksize file fix
if bytesRead > filesizeBytes:
    bytesRead = filesizeBytes

bytesPerLine = bytesRead/count
#print(bytesPerLine)

totalLinesEst = filesizeBytes / bytesPerLine
#print("Estimated lines in file: " + str(totalLinesEst))

# exact outpout count
resultlines = 0

fh = open(filename)
while resultlines < int(args.n):
    readstart = int(random.randint(0, int(totalLinesEst)) - bytesPerLine)
    if readstart < bytesPerLine:
        readstart = 0
    else:
        fh.seek(readstart)
    scratch = fh.readline()
    print(fh.readline(), end='', flush=True)
    resultlines += 1
fh.close()
