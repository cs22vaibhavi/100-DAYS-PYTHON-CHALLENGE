def check_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = "madam"

print(check_palindrome(text))
