sum = 0
count = 0
max = 0
min = 0
while True:
    s = input("enter: ")
    if not s:
        print(len(s), sum, count, max, min, (sum/count))
        break
    number = int(s)
    sum += number
    count += 1

    if number > max:
        max = number
