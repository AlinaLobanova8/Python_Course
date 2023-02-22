def pair(value):
    sq_num = int(value ** 0.5)
    res = 1 + (0 if sq_num ** 2 != value else sq_num)

    for i in range(2, sq_num):
        if value % i == 0:
            res += i + value // i
    return res

for j in range(10, 300):
    sum1 = pair(j)
    sum2 = pair(sum1)
    if sum2 == j and sum1 < sum2:
        print(j, sum1)