_ = input()
n = [int(i) for i in input().split()]

_ = input()
m = [int(j) for j in input().split()]

print(*[i for i in n if i not in m])