sum = 0
count = 0
max =None
min = None
while True:
    s = input("enter a number: ")
    if not s:
        print("Number of numbers entered", count, "Sumary of numbers",sum, "Maimum number",max, "Minimum number",min, "Average value of numbers",sum/count)
        break
    number = int(s)
    sum += number
    count += 1
    if max is None or number > max:
        max = number
    if min is None or number < min:
        min = number


