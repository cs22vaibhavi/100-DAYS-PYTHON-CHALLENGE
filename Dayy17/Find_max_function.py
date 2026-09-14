def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [15, 42, 8, 30]

print("Largest =", find_max(numbers))
