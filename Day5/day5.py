# Part 1
import re
import copy
line_break = False
# lst = [[],[],[]]
lst = [[],[],[], [],[],[], [],[],[]]
actions_lst = []

with open("day5input.txt", "r") as f:

    # Parsing text file
    for line in f:
        line = line.rstrip()

        if '1' in line:
            line_break = True

        if line_break == False: 
           
            try:
                lst[0].append(line[1])
                lst[1].append(line[5])
                lst[2].append(line[9])
                lst[3].append(line[13])
                lst[4].append(line[17])
                lst[5].append(line[21])
                lst[6].append(line[25])
                lst[7].append(line[29])
                lst[8].append(line[33])
            except:
                pass
        elif 'move' in line:
            actions_lst.append(line)

    # print(lst)
    for idx, sublist in enumerate(lst):
        lst[idx] = [x for x in sublist if ' ' not in x]
        lst[idx] = lst[idx][::-1]

    print(lst)
    lst2 = copy.deepcopy(lst) # copy list for part2
    # print(actions_lst)

    # Rearrange boxes for Part 1
    for action in actions_lst:
        numbers = re.findall(r'\d+', action)
        # print(numbers)

        for i in range(int(numbers[0])):
            box = lst[int(numbers[1]) - 1].pop()
            lst[int(numbers[2]) - 1].append(box)

        # print(lst)

    top_boxes = ''
    for boxes in lst:
        top_boxes += boxes[len(boxes) - 1]

    print(top_boxes)

    # Rearrange boxes for Part 2
    for action in actions_lst:
        numbers = re.findall(r'\d+', action)
        # print(numbers)

        box = lst2[int(numbers[1]) - 1][-int(numbers[0]):]
        # print(box)
        lst2[int(numbers[1]) - 1] = lst2[int(numbers[1]) - 1][:len(lst2[int(numbers[1]) - 1]) - int(numbers[0])]
        lst2[int(numbers[2]) - 1].extend(box)
        # print(lst2)

        # print(lst)

    top_boxes_lst2 = ''
    # print(lst2)
    for boxes in lst2:
        top_boxes_lst2 += boxes[len(boxes) - 1]

    print(top_boxes_lst2)

   



    


