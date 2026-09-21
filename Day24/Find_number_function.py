def find_number(numbers, target):
    if target in numbers:
        return "Number Found"
    else:
        return "Number Not Found"


numbers = [10, 20, 30, 40]

print(find_number(numbers, 30))
