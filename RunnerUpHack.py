n = int(input())
arr = list(map(int, input().split()))
new_arr = list(filter(lambda a: a != max(arr), arr))

print(max(new_arr))

