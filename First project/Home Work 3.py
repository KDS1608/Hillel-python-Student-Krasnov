num = int(input("Enter a number:"))

a = num // 100
b = num % 100 // 10
c = num % 10

print('The number is: ', c * 100 + b * 10 + a)
