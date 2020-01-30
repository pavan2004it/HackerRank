x = int(input())
c_list = []
for _ in range(x):
    name = input()
    score = float(input())
    c_list.append([name, score])

# z = min(c_list, key=lambda y: y[1])[1]
# # print(z)
# for element in c_list:
#     print(c_list)
#     if element[1] == z:
#         c_list.remove(element)

# print(c_list)
first_min = min(c_list, key=lambda y: y[1])[1]
least_arr = [x for x in c_list if x[1] != first_min]
min_fil = min(least_arr, key=lambda y: y[1])[1]
second_least = [x for x in least_arr if x[1] == min_fil]
second_least.sort(key=lambda y: y[0])
for element in second_least:
    print(element[0])
# second_least = [x[0] for x in least_arr if x == min(least_arr, key=lambda y: y[1])]
# print(second_least)
# print(min(new_arr, key=lambda y: y[1]))

# score_list = [37.21, 37.21, 37.2, 41, 39]
# score_list.remove(min(score_list, key=lambda x: x[1]))
# print(score_list)
# print(min(score_list))

# a = [8, 2, 1, 3, 4]
# z = [x for x in a if x == min(a)]
# print(z)
