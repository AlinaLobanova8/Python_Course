list = [1, 2, 3, 4, 5]
k = 3
print(list)
result = list[(k % len(list)):] + list[:(k % len(list))]
print(result)