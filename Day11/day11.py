# Part 1
import re

from monkey import Monkey
Monkey_dict = {}
number = 0
starting_lst = []
operation = ""

# Parsing data

with open("day11sampleinput.txt") as f:
    for line in f:
        line = line.rstrip()

        if line[:6] == "Monkey":
            number = int(line[7])
            monkey_trigger = True
            
        if "Starting items" in line:
            starting_lst = re.findall(r'\d+', line)
            starting_lst = [ int(x) for x in starting_lst ]

        if "Operation" in line:
            operation = line[19:]
        
        if "divisible" in line:
            divisible = int(re.findall(r'\d+', line)[0])
        
        if "true" in line:
            true_throw = int(re.findall(r'\d+', line)[0])

        if "false" in line:
            false_throw = int(re.findall(r'\d+', line)[0])

        if len(line) == 0:
            Monkey_dict[number] = Monkey(number, starting_lst, operation, divisible, true_throw, false_throw,0)

Monkey_dict[number] = Monkey(number, starting_lst, operation, divisible, true_throw, false_throw,0)

# Iterating through the items
rounds = 1000

def addResult(result):
    for i in result:
        Monkey_dict[i[1]].addItems(i[0])

for i in range(rounds):
    for k,v in Monkey_dict.items():
        addResult(v.result())

    print(f"\n-----After Round {i+1}-----")
    # for k,v in Monkey_dict.items():
    #     print("Monkey:",k, "Items:", v.getItems(), "InspectionNum:", v.getNumInpsections())

inspection_num_lst = []

for k,v in Monkey_dict.items():
    inspection_num_lst.append(v.getNumInpsections())

inspection_num_lst.sort(reverse=True)
print(inspection_num_lst[0] * inspection_num_lst[1])
