import numpy as np

def isBorderElement(row, col, arr) -> bool:

    col_len = len(arr[0])
    rows_len = len(arr)

    if row == 0 or col == 0 or row == (rows_len - 1) or col == (col_len - 1):
        return True


def isTreeVisible(row, col, arr) -> tuple:

    count_visible = 0
    count_trees_dict = {}

    # check top
    i = 1
    while (isBorderElement(row - i, col, arr) != True and arr[row][col] > arr[row - i][col]):
        i += 1
        count_trees_dict['top'] = i

    if arr[row][col] > arr[row - i][col]:
        count_visible += 1

    if i == 1:
        count_trees_dict['top'] = 1

    # check bottom
    i = 1
    while (isBorderElement(row + i, col, arr) != True and arr[row][col] > arr[row + i][col]):
        i += 1
        count_trees_dict['bottom'] = i
    
    if arr[row][col] > arr[row + i][col]:
        count_visible += 1

    if i == 1:
        count_trees_dict['bottom'] = 1

    # check right
    i = 1
    while (isBorderElement(row, col + i, arr) != True and arr[row][col] > arr[row][col + i]):
        i += 1
        count_trees_dict['right'] = i

    if arr[row][col] > arr[row][col + i]:
        count_visible += 1

    if i == 1:
        count_trees_dict['right'] = 1

    # check left
    i = 1
    while (isBorderElement(row, col - i, arr) != True and arr[row][col] > arr[row][col - i]):
        i += 1
        count_trees_dict['left'] = i

    if arr[row][col] > arr[row][col - i]:
        count_visible += 1

    if i == 1:
        count_trees_dict['left'] = 1
    
    # print(count_visible, count_trees_dict)
    if count_visible > 0:
        return True, count_trees_dict
    else:
        return False, count_trees_dict

if __name__ == "__main__":

    # PARSING THE DATASET
    rows = 0
    cols = 0

    file = "day8input.txt"

    # Getting number of rows and cols for array
    with open(file) as f:
        for line in f:
            line = line.rstrip()

            rows += 1

        cols = len(line)

    # initialize array
    my_array = np.empty((rows, cols), int)

    # adding input to array
    row = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()

            line_list = list(line)
            for col_idx, col in enumerate(line_list):
                my_array[row][col_idx] = line_list[col_idx]

            row += 1


    # RUNNING THE CODE 
    count = 0
    max_total = 0
    for j in range(len(my_array[0])):
        for i in range(len(my_array)):
            
            # Check that element is not a border element
            if isBorderElement(i, j, my_array) != True:

                # Check Tree visiblity
                # print(f"Checking for {i},{j},{my_array[i][j]}")
                if isTreeVisible(i,j,my_array)[0] == True:
                    count += 1

                # Calculate total core for each tree
                total = 1
                for k,v in isTreeVisible(i,j,my_array)[1].items():
                    total *= v

                if total > max_total:
                    max_total = total

            else:
                count += 1

    print(count)
    print(max_total)

        
