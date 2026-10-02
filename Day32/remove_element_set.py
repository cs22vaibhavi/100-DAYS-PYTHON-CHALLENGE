def remove_element(numbers, value):
    numbers.remove(value)
    return numbers


numbers = {10, 20, 30, 40}

print("After removing =", remove_element(numbers, 30))
