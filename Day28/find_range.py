def find_range(numbers):
    largest = max(numbers)
    smallest = min(numbers)

    return largest - smallest


numbers = [10, 25, 5, 40, 15]

print("Range =", find_range(numbers))
