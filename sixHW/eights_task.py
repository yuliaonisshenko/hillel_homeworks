def display_box(width, height, character):
    horizontal_line = character * width
    print(horizontal_line)
    for _ in range(height - 2):
        middle_line = f"{character}{'_' * (width - 2)}{character}"
        print(middle_line)
    print(horizontal_line)
display_box(6, 4, 'x')
