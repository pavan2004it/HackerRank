stu_a = int(input())
set_a = {x for x in input().split()}
stu_b = int(input())
set_b = {x for x in input().split()}

print(len(set_a - set_b))
