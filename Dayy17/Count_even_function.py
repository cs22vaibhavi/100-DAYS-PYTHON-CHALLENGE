def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

    return count


numbers = [1, 2, 4, 7, 8, 10]

print("Even numbers =", count_even(numbers))
