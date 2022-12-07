# Part 1

with open("day6input.txt") as f:
    for line in f:
        
        for i in range(4, len(line)):
            line_set = line[i-4:i]
            if len(set(line_set)) == len(line_set):
                break


# Part 2

with open("day6input.txt") as f:
    for line in f:
        
        print(line)
        for i in range(14, len(line)):
            line_set = line[i-14:i]
            if len(set(line_set)) == len(line_set):
                print(i)
                break