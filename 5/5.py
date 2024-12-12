

#Open the rules input 
with open('5/input.txt') as file:
    lines = file.readlines()

# make tuples of rules and list of tuples
rules = []
for l in lines:
    rule = (int(l.split("|")[0]), int(l.strip().split("|")[1]))
    rules.append(rule)


# open the instructions file
with open('5/input2.txt') as file:
    lines = file.readlines()

# make an ins list of lists   
ins = []
for l in lines:
    instruction = l.strip().split(",")
    # convert all strings to int
    ins.append(list(map(int,instruction)))

validPrint = 0
middles = 0
for instruction in ins: # each line of printing
    print('')
    print('new job')
    validRules = []
    for i, idx in enumerate(instruction[:-1]): # for each print page
        curItem = instruction[i]
        for item in range(len(instruction[:i+2])): # for each possible combination of print pages
            nextItem = instruction[item]
            curTup = (curItem,nextItem)
            present = curTup in rules # see if each pair of pages is a rule in the rule list
            if present:
                validRules.append(curTup) # make a list of the rules we need to check

    for rule in validRules: # start going through each valid rule and make sure the print tuples match
        valid = True
        left = rule[0]
        right = rule[1]
        print('')
        print(rule)
        print (left, instruction.index(left))
        print(right, instruction.index(right))
        if instruction.index(left) > instruction.index(right):
            print("invalid print job")
            valid = False
            break
    if valid:
        middleIdx = len(instruction) // 2
        middle = instruction[middleIdx]
        validPrint += 1
        middles += middle

print(validPrint, middles)
    
        

        