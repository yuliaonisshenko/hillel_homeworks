"""Create a decorator that prints to the console the name of the function that was called. The function should work as intended. For example, create a pair of functions for the arithmetic operations of summation and multiplication. When calling these functions, the result of the operation must be returned and the name of the function that was called must be displayed in the console with the result"""
def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Called function: {func.__name__}, Result: {result}")
        return result
    return wrapper
@print_function_name
def add_numbers(a, b):
    return a + b
@print_function_name
def multiply_numbers(a, b):
    return a * b
print(add_numbers(7, 3))
print(multiply_numbers(6, 5))
