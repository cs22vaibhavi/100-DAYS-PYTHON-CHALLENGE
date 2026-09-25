def even_sum(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total


numbers = [2, 5, 8, 10, 3]

print("Even sum =", even_sum(numbers))
