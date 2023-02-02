list = [1, 2, 3, 4, 5]
k = 3
print(list)
result = list[(k % len(list)):] + list[:(k % len(list))]
print(result)

# list = [1, 2, 3, 4, 5]
# k = 3
# print(list)

# for i in range(k % len(list) - 1):
#     list.insert(0, list.pop(- 1))

# print(list)