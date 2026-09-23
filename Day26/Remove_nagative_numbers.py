def remove_negative(numbers):
    result = []

    for number in numbers:
        if number >= 0:
            result.append(number)

    return result


numbers = [-5, 10, -2, 8, -1, 20]

print("Positive numbers =", remove_negative(numbers))
