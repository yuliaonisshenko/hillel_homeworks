#1 task
import os
import random

folder = "./test/data"
os.makedirs(folder, exist_ok=True)
data = []
for i in range(100):
    left_operand = random.randint(1, 10)
    right_operand = random.randint(1, 10)
    operation = random.randint(1, 3)
    data.append((left_operand, right_operand, operation))
    filename = "./test/data/data.txt"
    with open(filename, "w") as file:
        for tuple_data in data:
            line = " ".join(str(element) for element in tuple_data)
            file.write(line + "\n")
