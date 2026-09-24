def find_lengths(words):
    result = []

    for word in words:
        result.append(len(word))

    return result


words = ["cat", "python", "java"]

print("Lengths =", find_lengths(words))
