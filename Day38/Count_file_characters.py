file = open("message.txt", "r")

data = file.read()

file.close()

print("Number of characters =", len(data))
