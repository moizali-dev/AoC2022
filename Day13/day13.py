pairs_dict = {}
lst = []
pair_count = 1
import ast
import itertools
from utils import sort

with open("/Users/moizali/Documents/Personal/AoC2022/Day13/day13input.txt") as f:
    for lines in f:
        line = lines.rstrip()

        if len(line) == 0:
            pairs_dict[pair_count] = lst
            lst = []
            pair_count += 1
        else:
            line_input = ast.literal_eval(line)

            lst.append(line_input)

    pairs_dict[pair_count] = lst     


def recurseCountItemslist(lst, count = []):
    for item in lst:
        if isinstance(item, list):
            recurseCountItemslist(item, count)
        else:
            count.append(1)
            print(item)
    return len(count)

def InRightOrderLists(firstList, secondList, result = 0):

    for i,j in itertools.zip_longest(firstList, secondList):
        # print(i,j)

        #base case
        if result == -1 or result == 1:
            pass

        elif isinstance(i, int) == True and isinstance(j, int) == True:
            if j == i:
                pass
            elif j < i:
                result = -1
                return result
            else:
                result = 1
                return result

        elif i == None:
            result = 1
            return result
        elif  j == None:
            result = -1
            return result
        
        elif isinstance(i, list) == True and isinstance(j, list) == True:
            result = InRightOrderLists(i, j, result)   

        elif isinstance(i, list) == True and isinstance(j, int) == True:
            j = [j]
            result = InRightOrderLists(i, j, result) 

        elif isinstance(i, int) == True and isinstance(j, list) == True:
            i = [i]
            result = InRightOrderLists(i, j, result) 

    return result

count = 0
masterLst = []
for k,v in pairs_dict.items():
    print("\n", "--NEW COMPARE--", v[0], v[1])
    result = InRightOrderLists(v[0],v[1])
    print(result)
    if result == 1:
        count += k
    print(count)
    masterLst.append(v[0])
    masterLst.append(v[1])

print(count)
masterLst.append([[2]])
masterLst.append([[6]])
print(masterLst)

sortfn = sort()
sorted_masterLst = sortfn.merge_sort(masterLst)

total = 1
for idx, i in enumerate(sorted_masterLst):
    if i == [[2]]:
        total *= idx+1
    if i == [[6]]:
        total *= idx+1

print(total)