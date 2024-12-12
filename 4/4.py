import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def search_around(char,inputArr,row,index,location = 0):
    if location == 0:
        Ms = []
        if char in inputArr[row-1][index-1]:
            location = 1
            rowLoc = row-1
            indexLoc = index-1
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row-1][index]:
            location = 2
            rowLoc = row-1
            indexLoc = index
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row-1][index+1]:
            location = 3
            rowLoc = row-1
            indexLoc = index+1
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row][index-1]:
            location = 4
            rowLoc = row
            indexLoc = index-1
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row][index+1]:
            location = 6
            rowLoc = row
            indexLoc = index+1
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row+1][index-1]:
            location = 7
            rowLoc = row + 1 
            indexLoc = index - 1
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row+1][index]:
            location = 8
            rowLoc = row + 1
            indexLoc = index
            Ms.append([location, rowLoc, indexLoc])
        if char in inputArr[row+1][index+1]:
            location = 9
            rowLoc = row + 1
            indexLoc = index + 1
            Ms.append([location, rowLoc, indexLoc])
        return Ms
    elif location == 1:
        if char in inputArr[row-1][index-1]:
            location = 1
            rowLoc = row-1
            indexLoc = index-1
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 2:
        if char in inputArr[row-1][index]:
            location = 2
            rowLoc = row-1
            indexLoc = index
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 3:
        if char in inputArr[row-1][index+1]:
            location = 3
            rowLoc = row-1
            indexLoc = index+1
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 4:
        if char in inputArr[row][index-1]:
            location = 4
            rowLoc = row
            indexLoc = index-1
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 6:
        if char in inputArr[row][index+1]:
            location = 6
            rowLoc = row
            indexLoc = index+1
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 7:
        if char in inputArr[row+1][index-1]:
            location = 7
            rowLoc = row + 1 
            indexLoc = index - 1
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 8:
        if char in inputArr[row+1][index]:
            location = 8
            rowLoc = row + 1
            indexLoc = index
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    elif location == 9:
        if char in inputArr[row+1][index+1]:
            location = 9
            rowLoc = row + 1
            indexLoc = index + 1
            return location, rowLoc, indexLoc
        else: 
            location = 0 
            return location, row, index
    else: 
        location = 0 
        return location, row, index

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

success = 0

arr = np.array(lineList)
arr = np.pad(arr,1)
for row, line in enumerate(arr):
    for index, char in enumerate(line):
       
        # if char == 'X':
        #     print(' ')
        #     print(char, row, index)
        #     # print(arr[row-1][index-1],arr[row-1][index],arr[row-1][index+1])
        #     # print(arr[row][index-1],arr[row][index],arr[row][index+1])
        #     # print(arr[row+1][index+1],arr[row+1][index],arr[row+1][index+1])
        #     for a in search_around('M',arr,row,index):
        #         print(a)

        #         direction,nextRow,nextIndex = a
        #         if not direction == 0:
                    
        #             print('M', nextRow, nextIndex, direction)
        #             direction, nextRow,nextIndex = search_around('A',arr,nextRow,nextIndex, direction)
        #             if not direction == 0:
        #                 print('A',nextRow,nextIndex,direction)
        #                 print(search_around('S',arr,nextRow,nextIndex,direction))
        #                 direction,nextRow,nextIndex = search_around('S',arr,nextRow,nextIndex,direction)
        #                 if not direction == 0:
        #                     print('S', nextRow, nextIndex,direction)
        #                     success += 1

        if char == 'A':
            print('')
            print(arr[row-1][index-1],arr[row-1][index],arr[row-1][index+1])
            print(arr[row][index-1],arr[row][index],arr[row][index+1])
            print(arr[row+1][index+1],arr[row+1][index],arr[row+1][index+1])
            if arr[row - 1][index - 1] == 'S' and arr[row+1][index+1] == 'M':
                if arr[row-1][index+1] == 'S' and arr[row+1][index-1] == 'M':
                    success += 1
                    print("success")
                elif arr[row -1][index+1] == 'M' and arr[row+1][index-1] == 'S':
                    success += 1
                    print("success")
            if arr[row - 1][index - 1] == 'M' and arr[row+1][index+1] == 'S':
                if arr[row-1][index+1] == 'S' and arr[row+1][index-1] == 'M':
                    success += 1
                    print("success")
                elif arr[row -1][index+1] == 'M' and arr[row+1][index-1] == 'S':
                    success += 1
                    print("success")
print(success)


                