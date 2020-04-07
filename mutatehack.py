set_elem = int(input())
set_a = {int(x) for x in input().split()}
set_number = int(input())

for _ in range(2 * set_number):
    ops = input().split()
    set_b = {int(x) for x in input().split()}
    eval('set_a.{0}({1})'.format(ops[0], set_b))

print(sum(set_a))
