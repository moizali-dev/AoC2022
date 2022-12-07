total = 0
dir_list = []
with open("day7input.txt") as f:
    for line in f:
        line_input = line.rstrip()

        if "dir" in line_input:
            dir_list.append(line_input)

print(len(set(dir_list)))