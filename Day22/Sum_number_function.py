def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

result = sum_numbers(10)

print("Sum =", result)
