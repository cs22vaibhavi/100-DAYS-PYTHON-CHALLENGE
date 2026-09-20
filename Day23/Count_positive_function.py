def count_positive(numbers):
    count = 0

    for number in numbers:
        if number > 0:
            count = count + 1

    return count


numbers = [-2, 5, 8, -1, 10, 3]

print("Positive numbers =", count_positive(numbers))
