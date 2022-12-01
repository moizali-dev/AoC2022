### Part 1 ###

max_cals = 0
total_cals = 0

with open("Day1/input.txt", 'r') as f:
    for line in f:
        cals = line.strip()
        
        if cals == "":
            if total_cals >= max_cals:
                max_cals = total_cals
            total_cals = 0 
        else:
            total_cals += int(cals)

print(f"How many total Calories is that Elf carrying? {max_cals}")

### Part 2 ###
        
total_cals = 0
cals_lst = []

with open("Day1/input.txt", 'r') as f:
    for line in f:
        cals = line.strip()
        
        if cals == "":
            cals_lst.append(total_cals)
            total_cals = 0

        else:
            total_cals += int(cals)

    cals_lst.append(total_cals)
    cals_lst.sort(reverse=True)


print(f"How many Calories are those Elves carrying in total? {sum(cals_lst[:3])}")