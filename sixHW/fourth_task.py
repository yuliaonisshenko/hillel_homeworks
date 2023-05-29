file_test = 'test/test.txt'  # path to the my test file

def remove_numbers_from_file(file_test):
    cleared_lines = []
    with open(file_test, 'r') as file:
        for line in file:
            line_without_numbers = ''.join(char for char in line if not char.isdigit())
            cleared_lines.append(line_without_numbers.strip())
        return cleared_lines
cleared_lines = remove_numbers_from_file(file_test)
for line in cleared_lines:
    print(line)
