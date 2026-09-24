def capitalize_words(words):
    result = []

    for word in words:
        result.append(word.capitalize())

    return result


words = ["python", "java", "html"]

print("Capitalized =", capitalize_words(words))
