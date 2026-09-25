def shortest_word(words):
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return shortest


words = ["apple", "cat", "banana", "dog"]

print("Shortest word =", shortest_word(words))
