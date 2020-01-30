N, M = map(int, input().split())
j = 1
for i in range(N):
    if i < (N - 1) / 2:
        print("-" * int((M-3)/2 - (i*3)) + ".|."*(j + i*2) + "-" * int((M-3)/2 - (i*3)))
    elif i == (N-1) / 2:
        print("-" * int((M-7)/2) + "Welcome".upper() + "-" * int((M-7)/2))
    else:
        print("-" * int((M - (N-j*2)*3)/2) + ".|." * (N - j*2) + "-" * int((M - (N-j*2)*3)/2))
        j += 1


