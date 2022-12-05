# Part 1

total = 0

with open("day3input.txt", "r") as f:
    for line in f:
        str_input = line.strip()

        len_str = len(str_input)
        mid_str = int(len_str / 2)
        
        first_half_str = str_input[:mid_str]
        second_half_str = str_input[mid_str:]

        common_char = set(first_half_str).intersection(second_half_str)
        common_char = list(common_char)[0]

        # if lower case then 96 - ord(char)... if upper case then ord(65) - 38
        if common_char.isupper():
            # print(ord(common_char) - 38, common_char)
            total += ord(common_char) - 38
        elif common_char.islower():
            # print(ord(common_char) - 96, common_char)
            total += ord(common_char) - 96

print(total)

# Part 2
total = 0
lst = []

with open("day3input.txt", "r") as f:
    for line in f:
        str_input = line.strip()

        if len(lst) < 3:
            lst.append(str_input)
            print(lst)
        else:
            s1 = set(lst[0])
            s2 = set(lst[1])
            s3 = set(lst[2])

            common_char = s1.intersection(s2, s3)
            common_char = list(common_char)[0]

            if common_char.isupper():
                # print(ord(common_char) - 38, common_char)
                total += ord(common_char) - 38
            elif common_char.islower():
                # print(ord(common_char) - 96, common_char)
                total += ord(common_char) - 96

            print(common_char)
            lst = []

            lst.append(str_input)

    s1 = set(lst[0])
    s2 = set(lst[1])
    s3 = set(lst[2])

    common_char = s1.intersection(s2, s3)
    common_char = list(common_char)[0]
    if common_char.isupper():
        # print(ord(common_char) - 38, common_char)
        total += ord(common_char) - 38
    elif common_char.islower():
        # print(ord(common_char) - 96, common_char)
        total += ord(common_char) - 96

print(total)    

