from board import Board
import gc
from tqdm import tqdm

SensorBeaconDict = {}

min_x = 1000000000000
min_y = 1000000000000
max_x = 0
max_y = 0

# Row is y; Col is x;

import re
with open("day15input.txt") as f:
    for lines in f:
        line = lines.rstrip()

        numbers = re.findall(r'-?\d+\.?\d*', line)
        SensorCoord = int(numbers[0]) , int(numbers[1])
        BeaconCoord = int(numbers[2]) , int(numbers[3])

        if min_x > min(int(numbers[0]), int(numbers[2])):
            min_x = min(int(numbers[0]), int(numbers[2]))

        if min_y > min(int(numbers[1]), int(numbers[3])):
            min_y = min(int(numbers[1]), int(numbers[3]))

        if max_x < max(int(numbers[0]), int(numbers[2])):
            max_x = max(int(numbers[0]), int(numbers[2]))

        if max_y < max(int(numbers[1]), int(numbers[3])):
            max_y = max(int(numbers[1]), int(numbers[3]))

        SensorBeaconDict[SensorCoord] = BeaconCoord

print((min_x, min_y), (max_x, max_y))

# Creating board
board = Board(0, min_y, 4500000, 4400000)

for k,v in SensorBeaconDict.items():
    print(k,v)
    board.updateBoard(k,1)
    board.updateBoard(v,2)

print("Sensor Start")
row = 2000000
# board.sensorBeaconScanRow((8,7),(2,10),10)
for k,v in tqdm(SensorBeaconDict.items()):
    print(k,v)
    board.sensorBeaconScanRow(k,v, row)


# counting number of # for row 10:
# print(board.printBoard())

count = 0
for i in board.getRow(row):
    if i == 3:
        count += 1

print(count)

## 3844596 ##
## 3844597 ##





