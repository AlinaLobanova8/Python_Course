list_num = [0, -1, 5, 2, 3]
print(sum([1 for i in range(len(list_num)) if list_num [i] > list_num [i - 1]]))