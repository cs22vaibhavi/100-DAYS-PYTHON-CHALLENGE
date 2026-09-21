def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


numbers = [25, 10, 45, 5, 30]

print("Smallest =", find_smallest(numbers))
