def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


numbers = [25, 10, 45, 5, 30]

print("Smallest =", find_min(numbers))
