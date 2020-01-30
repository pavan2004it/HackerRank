import os


def solve(s):
    a = [x.capitalize() for x in s.split(" ")]
    return " ".join(a)


fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = solve(s)

fptr.write(result + '\n')

fptr.close()