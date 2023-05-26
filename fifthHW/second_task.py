#2 task
import os
file_name = "./test/data/data.txt"
with open(file_name, "r") as file:
    for data in file:
        numbers = data.strip().split()
        left_operand = int(numbers[0])
        right_operand = int(numbers[1])
        operation = int(numbers[2])
        result = None
        if operation == 1:
            result = left_operand + right_operand
        if operation == 2:
            result = left_operand - right_operand
        if operation == 3:
            result = left_operand * right_operand
        print(f"{left_operand} {'+' if operation == 1 else '-' if operation == 2 else '*'} {right_operand} = {result}")
