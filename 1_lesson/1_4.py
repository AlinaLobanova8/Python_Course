a = int(input("Какой год: \n"))

if (a % 4 == 0 and a % 100) or a % 400 == 0:
    print("Yes")
else:
    print("No")