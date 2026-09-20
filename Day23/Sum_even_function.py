def sum_even(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total = total + number

    return total


numbers = [1, 2, 3, 4, 5, 6]

print("Sum of even numbers =", sum_even(numbers))
