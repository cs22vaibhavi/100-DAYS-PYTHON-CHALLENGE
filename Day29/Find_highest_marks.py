def highest_mark(marks):
    highest = 0

    for mark in marks.values():
        if mark > highest:
            highest = mark

    return highest


marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print("Highest mark =", highest_mark(marks))
