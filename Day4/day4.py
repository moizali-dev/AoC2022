# Part 1

count = 0
with open("day4sampleinput.txt", "r") as f:
    for line in f:
        input = line.strip().split(',')

        first_input = input[0].split("-")
        second_input = input[1].split("-")

        
        if (int(first_input[0]) >= int(second_input[0]) and int(first_input[1]) <= int(second_input[1])):
            count += 1

        elif (int(second_input[0]) >= int(first_input[0]) and int(second_input[1]) <= int(first_input[1])):
            count += 1

print(count)

# Part 2

count = 0
total = 0
with open("day4input.txt", "r") as f:
    for line in f:
        input = line.strip().split(',')

        first_input = input[0].split("-")
        second_input = input[1].split("-")

        print(first_input, second_input)
        if (int(first_input[1]) < int(second_input[0])):
            print(True)
            count += 1
        elif  (int(first_input[0]) > int(second_input[1])):
            print(True)
            count += 1

        total += 1

print(total - count)