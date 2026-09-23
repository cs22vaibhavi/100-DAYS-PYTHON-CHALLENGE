def square_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number * number)

    return result


numbers = [1, 2, 3, 4, 5]

print("Squares =", square_numbers(numbers))
