def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count = count + 1

    return count

text = "Python Programming"

print("Vowels =", count_vowels(text))
