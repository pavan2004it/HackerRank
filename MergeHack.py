from collections import Counter
s = "AABCAAADA"
x = zip(*[iter(s)] * 3)
for _ in x:
    print("".join(list(dict.fromkeys(_).keys())))
