

def check_report(input):
   
    
    for item in range(len(input)-1):
        if input[item] < input[-1]: 
            direction = "asc"
        elif input[item] > input[-1]:
            direction = "des"
        else:
            return False, item
        
        curItem = input[item]
        nextItem = input[item+1]
        if item >= 1:
            if direction == "asc":
                if (curItem < nextItem) and (nextItem - curItem <= 3):
                    continue
                else: return False, item+1
            elif direction == "des":
                if (curItem > nextItem) and (curItem - nextItem <=3):
                    continue
                else: return False, item+1
        else:
            if direction == "asc":
                if (curItem < nextItem) and (nextItem - curItem <= 3):
                    continue
                else: return False, item
            elif direction == "des":
                if (curItem > nextItem) and (curItem - nextItem <=3):
                    continue
            else: return False, item

    return True, item+1

def new_check_report(input):

    if input[0] < input[-1]: 
            direction = "asc"
    elif input[0] > input[-1]:
            direction = "des"
    else:
        return False
    for item in range(len(input)-1):
        
        
        curItem = input[item]
        nextItem = input[item+1]
        if item >= 1:
            if direction == "asc":
                if (curItem < nextItem) and (nextItem - curItem <= 3):
                    continue
                else: return False
            elif direction == "des":
                if (curItem > nextItem) and (curItem - nextItem <=3):
                    continue
                else: return False
        else:
            if direction == "asc":
                if (curItem < nextItem) and (nextItem - curItem <= 3):
                    continue
                else: return False
            elif direction == "des":
                if (curItem > nextItem) and (curItem - nextItem <=3):
                    continue
                else: return False

    return True

        

         

with open('2/input.txt') as file:
    lines = file.read().splitlines()

safeReport = 0

for line in lines:
    report = [int(x) for x in line.strip().split()]
    status = new_check_report(report)
    print (report, status)
    if not status:
        for i in range(len(report)):
            report = [int(x) for x in line.strip().split()]
            new_report = report
            new_report.pop(i)
            status = new_check_report(new_report)
            print(report,status)
            if status :
                safeReport += 1
                break
    else:
        safeReport +=1
    print(safeReport)


# for line in lines:
#     dampened = False 
#     report = [int(x) for x in line.strip().split()]
#     print(report)
#     dedup = set(line)
#     reportRes = "safe"
#     status, pop = check_report(report)
#     if not dampened and not status:
#         new_report = report.pop(pop)
#         print(report)
#         dampened == True
#         status, pop = check_report(report)
#         if status == False:
#             reportRes = "unsafe"
            
    


        


    
    # if reportRes == "safe":
    #     for item in range(len(report)-1):
    #         curItem = report[item]
    #         nextItem = report[item+1]

    #         if not check_items(curItem,nextItem,direction):
    #             if dampened:
    #                 reportRes = "unsafe"
    #             else:
    #                 dampened = True
    #                 report.pop(item + 1)
    #                 if not item == len(report)-1:
    #                     curItem = report[item]
    #                     nextItem = report[item+1]

    #                     if not check_items(curItem,nextItem,direction):
    #                         reportRes = "unsafe"
    #                         break
                        
    # if reportRes == "safe":
    #     safeReport += 1
        
    
    # print(reportRes)
    # print (safeReport)
                


