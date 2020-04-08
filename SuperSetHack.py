set_a = {x for x in input().split()}
no_of_sets = int(input())
result = ''
for _ in range(no_of_sets):
    set_b = {x for x in input().split()}
    result = set_a.issuperset(set_b)
    if result:
        continue
    else:
        break
print(result)
