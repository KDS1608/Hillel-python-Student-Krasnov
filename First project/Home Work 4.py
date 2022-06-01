n = int(input("enter the number : "))

prime = True

i = 2

while i < n:

    if n % i == 0:
       prime = False
       break
    i += 1
if prime:
    print("Number is prime")
else:
    print('Number is not prime')

