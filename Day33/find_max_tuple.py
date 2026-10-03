def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = (15, 40, 25, 60, 10)

print("Largest =", find_max(numbers))
