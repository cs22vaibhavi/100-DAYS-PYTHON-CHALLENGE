def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


words = ["cat", "python", "apple", "computer"]

print("Longest word =", longest_word(words))
