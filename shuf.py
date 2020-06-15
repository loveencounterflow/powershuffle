#!/bin/python3

import random
f = open("lines_78000000000.txt", "rt")
count = 0
while 1:
  buffer = f.read(65536)
  if not buffer: break
  count += buffer.count('\n')

for i in range(10):
  print(f.readline(random.randint(1, count)))
