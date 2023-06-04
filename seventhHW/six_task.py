"""You are given a string representing a sequence of N arrows, each pointing in one of the four
cardinal directions: up (^), down (v), left(<) or right (>).
Write a function that, given a string S denoting the directions of the arrows, returns
the minimum number of arrows that must be rotated to make them all point in the same
direction"""
def arrows_rotation(arr: str) -> int:
    arrow_counts = {'^': 0, 'v': 0, '<': 0, '>': 0}

    for arrow in arr:
        arrow_counts[arrow] += 1

    max_count = max(arrow_counts.values())
    total_arrows = len(arr)
    min_rotations = total_arrows - max_count

    return min_rotations

arr = "^vv<v<<"
result = arrows_rotation(arr)
print(result)
