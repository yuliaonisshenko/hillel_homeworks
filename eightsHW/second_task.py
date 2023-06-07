"""Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive."""
def generate_squares_of_even_elements():
    for num in range(0, 1000000001, 2):
        yield num ** 2

even_squares = generate_squares_of_even_elements()

# Testing the generator function
for _ in range(5):
    print(next(even_squares))
