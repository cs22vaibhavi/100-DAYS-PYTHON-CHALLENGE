def calculate_average(marks):
    total = sum(marks.values())
    return total / len(marks)

marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print("Average =", calculate_average(marks))
