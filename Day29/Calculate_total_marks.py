def total_marks(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print("Total marks =", total_marks(marks.values()))
