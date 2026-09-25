def sum_of_squares(numbers):
    total = 0

    for number in numbers:
        total = total + (number * number)

    return total


numbers = [1, 2, 3, 4]

print("Sum of squares =", sum_of_squares(numbers))
