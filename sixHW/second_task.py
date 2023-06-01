#2 task
import math
def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal
size_of_square = square(5)
print(size_of_square)
