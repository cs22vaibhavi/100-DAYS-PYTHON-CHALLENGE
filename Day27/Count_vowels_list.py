def count_vowels(words):
    count = 0

    for word in words:
        for letter in word:
            if letter.lower() in "aeiou":
                count += 1

    return count


words = ["apple", "banana", "mango"]

print("Total vowels =", count_vowels(words))
