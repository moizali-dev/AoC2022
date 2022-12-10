cycle = 0
x = 1
int_input = 0
str_input = ""
signal_str = 0
signal_cycle_lst_part1 = [20, 60, 100, 140, 180, 220]
signal_cycle_lst_part2 = [40, 80, 120, 160, 200, 240]
i = 0
sprite = '###.....................................'

with open("day10input.txt") as f:
    for line in f:
        
        str_input = line[:4].strip()
        if str_input != "noop":
            cycle += 1
            if cycle == signal_cycle_lst_part1[i]:
                signal_str += cycle * x
                print("Sep: ", str_input, int_input, cycle, x, signal_str)
                i += 1
            cycle += 1
            # print("During: ", cycle, x)
            if cycle == signal_cycle_lst_part1[i]:
                signal_str += cycle * x
                print("Sep: ", str_input, int_input, cycle, x, signal_str)
                i += 1

            int_input = int(line[4:])
            x += int_input
        else:
            if i >= len(signal_cycle_lst_part1):
                pass
            else:
                cycle += 1
                if cycle == signal_cycle_lst_part1[i]:
                    signal_str += cycle * x
                    print("Sep: ", str_input, int_input, cycle, x, signal_str)
                    i += 1
            print("During: ", cycle, x)

# def sprite_update(sprite, X):
#     len_sprite = len(sprite)
#     sprite = ''

#     X_1 = X + 1
#     X_2 = X + 2

#     for i in range(len_sprite):
#         if i == X or i == X_1 or i == X_2:
#             sprite += "#"
#         else:
#             sprite += "."

#     return sprite

# j = 0
# with open("day10samplelargeinput.txt") as f:
#     for line in f:
        
#         str_input = line[:4].strip()
#         if str_input != "noop":
#             cycle += 1

#             print(sprite[j], end='')
#             j+=1

#             if j == len(sprite) - 1:
#                 j = 0

#             if cycle == signal_cycle_lst_part2[i]:
#                 i+=1
#                 print()
            
#             cycle += 1
#             print(sprite[j], end='')
#             j+=1

#             if j == len(sprite) - 1:
#                 j = 0

#             int_input = int(line[4:])
#             x += int_input

#             # print(x)
#             sprite = sprite_update(sprite, x-1)
#             # print(sprite)
#             if cycle == signal_cycle_lst_part2[i]:
#                 i+=1
#                 print()
#             # print("During: ", cycle, x)
            
#         else:
#             cycle += 1
#             print(sprite[j], end='')
#             j+=1

#             if j == len(sprite) - 1:
#                 j = 0

#             if cycle == signal_cycle_lst_part2[i]:
#                 i+=1
#                 print()