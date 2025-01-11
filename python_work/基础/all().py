#所有都成立则返回True，有一个不满足就返回False

# Example: Checking if all elements in a list are positive
numbers = [1, 2, 3, 4, 5]
result = all(n > 0 for n in numbers)
print(result)  # Output: True, because all numbers are positive

# Example: Checking if all characters in a string are alphabetic
s = "HelloWorld"
result = all(c.isalpha() for c in s)
print(result)  # Output: True, because all characters are letters

def is_lucky_digit(c):
    return c == '4' or c == '7'

def is_lucky_number(x):
    return all(is_lucky_digit(c) for c in str(x))

print(is_lucky_number(4477))  # True, because all digits are lucky
print(is_lucky_number(1234))  # False, because '1', '2', and '3' are not lucky