#3 task
import os
file_name = "./test/data/text.txt"
with open(file_name, "r") as file:
    text = file.read()
letter_counts = {}
for data in text:
    if data.isalpha():
        data = data.lower()
        letter_counts[data] = letter_counts.get(data, 0) + 1
for letter, count in letter_counts.items():
    print(f"Letter: {letter} counted {count}")
