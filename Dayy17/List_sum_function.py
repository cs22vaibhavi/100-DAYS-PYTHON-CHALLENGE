def list_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


numbers = [10, 20, 30, 40]

print("Sum =", list_sum(numbers))
