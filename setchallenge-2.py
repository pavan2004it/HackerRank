# set_a = {2, 4, 5, 9}
# set_b = {2, 4, 11, 12}
# diff = [x for x in set_a.symmetric_difference(set_b)]
# for _ in diff:
#     print(_)
# for _ in set_a.difference(set_b):
#     diff.append(_)
# for _ in set_b.difference(set_a):
#     diff.append(_)
#
# for _ in sorted(diff):
#     print(_)

elem_a = int(input())
set_a = {int(x) for x in input().split()}
elem_b = int(input())
set_b = {int(y) for y in input().split()}
diff = [int(x) for x in set_a.symmetric_difference(set_b)]
print(diff)
for _ in sorted(diff):
    print(_)
