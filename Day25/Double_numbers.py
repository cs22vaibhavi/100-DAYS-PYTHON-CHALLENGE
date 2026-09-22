def double_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number * 2)

    return result


numbers = [1, 2, 3, 4, 5]

print("Doubled numbers =", double_numbers(numbers))
