def check_element(numbers, value):
    if value in numbers:
        return "Element Found"
    else:
        return "Element Not Found"


numbers = {10, 20, 30, 40}

print(check_element(numbers, 30))
