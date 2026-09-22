def count_greater(numbers, value):
    count = 0

    for number in numbers:
        if number > value:
            count = count + 1

    return count


numbers = [10, 25, 40, 15, 50]

print("Numbers greater than 20 =", count_greater(numbers, 20))
