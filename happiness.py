happiness = 0
x, y = map(int, input().split())
int_arr = [int(x) for x in input().split()]
set_a = {int(x) for x in input().split()}
set_b = {int(x) for x in input().split()}

for _ in int_arr:
    if _ in set_a:
        happiness += 1
    elif _ in set_b:
        happiness -= 1

print(happiness)