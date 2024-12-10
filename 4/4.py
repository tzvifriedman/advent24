import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

with open("4/input.txt") as file:
    lines = file.readlines()

lineList = []
for l in lines:
    l = l.strip()
    charList = []
    for c in l:
        charList.append(c)
    lineList.append(charList)

lines = [x.strip() for x in lines]

arr = np.array(lineList)
arr = np.pad(arr,1)
print (arr)