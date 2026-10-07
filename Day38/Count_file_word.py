file = open("message.txt", "r")

data = file.read()

file.close()

words = data.split()

print("Number of words =", len(words))
