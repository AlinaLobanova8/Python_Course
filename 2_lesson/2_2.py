n = int(input())
f_1 = 0
f_2 = 1
count = 2

while n >= f_2:
    if n == f_2:
        print(count)
        break
    f_1, f_2 = f_2, f_1 + f_2
    count += 1
else:
    print(-1)