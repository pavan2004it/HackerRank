n = int(input("Enter a Number: "))
new_n = []
for i in range(1,n):
    new_n.append(i)
new_n.append(n)
for j in new_n:
    print(j, end="")
