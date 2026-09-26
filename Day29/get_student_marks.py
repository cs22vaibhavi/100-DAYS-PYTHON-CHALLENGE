def get_marks(student, subject):
    return student[subject]


student = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print("Python marks =", get_marks(student, "Python"))
