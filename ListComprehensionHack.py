x = int(input())
y = int(input())
# z = int(input())
n = int(input())

# a = [(i, j, k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i + j + k) != n]
a = [(i, j) for i in range(x+1) for j in range(y+1) if(i + j) != n]
print(a)

# coordinates = []
# for x in range(11):
#     for y in range(11):
#         coordinates.append((x, y))
# print(coordinates)