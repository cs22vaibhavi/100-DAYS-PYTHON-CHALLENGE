def odd_sum(numbers):
    total = 0

    for number in numbers:
        if number % 2 != 0:
            total += number

    return total


numbers = [1, 4, 7, 8, 9]

print("Odd sum =", odd_sum(numbers))
