def check_subject(marks, subject):
    if subject in marks:
        return "Subject Found"
    else:
        return "Subject Not Found"

marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90
}

print(check_subject(marks, "Java"))
