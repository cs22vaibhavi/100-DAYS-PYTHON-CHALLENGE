def second_largest(numbers):
    numbers = sorted(numbers)
    return numbers[-2]


numbers = [10, 25, 8, 40, 15]

print("Second largest =", second_largest(numbers))
