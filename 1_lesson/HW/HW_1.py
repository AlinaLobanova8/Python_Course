# Найдите сумму цифр трехзначного числа.

num = int(input())
sum_num = 0

while num:
    sum_num += num % 10
    num //= 10

print(sum_num)