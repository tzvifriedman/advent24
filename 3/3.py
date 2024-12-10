import re

with open('3/input.txt') as file:
    ins = file.read()
pattern = ["mul\(","do()","don\'t" ]
regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')
substrings = [i.start() for i in re.finditer(regex, ins) ]
validIns = []
for s in substrings:
    # print(ins[s:s+8])
    for i in range(12):
        curChar = ins[s+i]
        if ins[s+i] == ")":
            if "," in ins[s:s+i]:
                print(ins[s:s+i])
                validIns.append(ins[s:s+i])
            elif "do" in ins[s:s+i]:
                print(ins[s:s+i])
                validIns.append(ins[s:s+i])
            elif "don't" in ins[s:s+i]:
                print(ins[s:s+i])
                validIns.append(ins[s:s+i])
            break
for i in validIns:
    print(i)
total = 0
enabled = True
for i in validIns:
    if i == "don't(":
        enabled = False
        continue
    elif i == "do(":
        enabled = True
        continue
    else:
        if enabled:
            x = i.split("(")[1].split(",")[0]
            y = i.split(",")[1]
            print (x, y)
            total += int(x) * int(y)
print(total)