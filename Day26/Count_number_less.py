def count_less(numbers, value):
    count = 0

    for number in numbers:
        if number < value:
            count += 1

    return count


numbers = [5, 12, 8, 20, 3]

print("Numbers less than 10 =", count_less(numbers, 10))
