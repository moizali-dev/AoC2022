from typing import List, Tuple
import time
from fractions import Fraction

class Monkey:

    def __init__(self,number:int, items:List, operation:str, divisible:int, TrueMonkey:int, FalseMonkey:int, inspectionNum:int) -> None:
        self.number = number
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.TrueMonekey = TrueMonkey
        self.FalseMonkey = FalseMonkey
        self.inspectionNum = inspectionNum

    def result(self) -> List[Tuple]:
        worry_level = 0
        monkey_output = []

        for worry_level in self.items:
            worry_level = self.parseOperation(int(worry_level))
            # worry_level = worry_level // 3

            if worry_level % self.divisible != 0:
                monkey_output.append((worry_level, self.FalseMonkey))
            else:
                monkey_output.append((worry_level, self.TrueMonekey))

        # num of items inspected
        self.inspectionNum += len(self.items)
        # remove item from list
        self.items = []



        return monkey_output

    def parseOperation(self, worry_level) -> int:

        start_time = time.time()
        operation_lst = self.operation.split(" ")

        if "+" in operation_lst[1] and operation_lst[2] != "old":
            worry_level += int(operation_lst[2])
        elif "-" in operation_lst[1] and operation_lst[2] != "old":
            worry_level -= int(operation_lst[2])
        elif "*" in operation_lst[1] and operation_lst[2] != "old":
            worry_level *= int(operation_lst[2])
        elif "/" in operation_lst[1] and operation_lst[2] != "old":
            worry_level /= int(operation_lst[2])

        elif "+" in operation_lst[1] and operation_lst[2] == "old":
            worry_level += worry_level
        elif "-" in operation_lst[1] and operation_lst[2] == "old":
            worry_level -= worry_level
        elif "*" in operation_lst[1] and operation_lst[2] == "old":
            worry_level *= worry_level
        elif "/" in operation_lst[1] and operation_lst[2] == "old":
            worry_level /= worry_level

        end_time = time.time()
        time_taken = round(end_time - start_time,2)
        if time_taken > 1:
            print(f"Run time = {time_taken}, Operation: ,{operation_lst[1]} and {operation_lst[2]}")

        return worry_level

    def addItems(self, worry):
        self.items.append(worry)

    def getItems(self):
        return self.items

    def getNumInpsections(self):
        return self.inspectionNum


