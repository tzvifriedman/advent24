import os

with open('1/input.txt') as input:
    i = input.readlines()

arr1 = []
arr2 = []

for line in i:
    line=line.strip().split()
    arr1.append(line[0])
    arr2.append(line[1])

arr1 = [int(x) for x in arr1]
arr2 = [int(x) for x in arr2]
arr1 = sorted(arr1)
arr2 = sorted(arr2)

total = 0 
# for i in range(len(arr1)):
#     diff = abs(int(arr1[i]) - int(arr2[i]))
#     total += diff
simTotal = 0 
for i in range(len(arr1)):
    similarScore = arr1[i] * (arr2.count(arr1[i]))       
    print(similarScore) 
    simTotal += similarScore

print(simTotal)      

