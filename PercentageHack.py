# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# percentage = student_marks.get(query_name)
# print(float("%0.2f" % float(sum(percentage)/3)))

x = 12
y = [1,2,3]
perc = sum(y)/3
print("%.2f" % perc)