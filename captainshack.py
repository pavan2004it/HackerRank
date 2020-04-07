import collections
k = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'
list_a = [x for x in k.split()]
counter = collections.Counter(list_a)
for k, v in counter.items():
    if v == 1:
        print(k)
