n = int(input())
max = min = int(input("Вес: "))

for _ in range(n - 1):
    count = int(input())
    if count > max:
        max = count
    if count < min:
        min = count
print(min, max)