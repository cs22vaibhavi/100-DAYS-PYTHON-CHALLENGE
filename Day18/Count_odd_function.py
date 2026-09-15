def count_odd(numbers):
    count = 0

    for number in numbers:
        if number % 2 != 0:
            count = count + 1

    return count


numbers = [1, 2, 3, 4, 5, 7]

print("Odd numbers =", count_odd(numbers))
