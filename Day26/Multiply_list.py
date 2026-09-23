def multiply_numbers(numbers):
    result = 1

    for number in numbers:
        result = result * number

    return result


numbers = [2, 3, 4]

print("Product =", multiply_numbers(numbers))
