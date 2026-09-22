def calculate_total(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


prices = [100, 200, 150, 50]

print("Total =", calculate_total(prices))
