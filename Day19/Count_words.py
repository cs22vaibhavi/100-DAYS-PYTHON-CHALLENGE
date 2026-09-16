def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "Python is easy to learn"

print("Words =", count_words(sentence))
