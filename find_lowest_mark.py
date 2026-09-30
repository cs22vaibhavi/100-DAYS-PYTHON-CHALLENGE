def lowest_mark(marks):
    lowest = 100

    for mark in marks.values():
        if mark < lowest:
            lowest = mark

    return lowest


marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print("Lowest mark =", lowest_mark(marks))
