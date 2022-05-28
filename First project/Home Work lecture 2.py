# Numbers of children in groups
"""
a - numbers of children group 1
b - numbers of children group 2
"""


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("The number is: ", (a // 2 + a % 2) + (b // 2 + b % 2))

