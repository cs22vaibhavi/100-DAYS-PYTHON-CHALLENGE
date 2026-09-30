def update_mark(marks, subject, new_mark):
    marks[subject] = new_mark
    return marks

marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print(update_mark(marks, "Java", 88))
