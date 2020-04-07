"""
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------


"""

import timeit
import string


def sol_one():
    number = 5
    m: int = 1
    x = number - 1
    vertical_lines = number + (number - 1)
    alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    for i in range(vertical_lines):
        if number == 1:
            print(alpha[number-1])

        elif x > 0 and i < (number - 1):
            if len(('-'.join(alpha[x:number]))) > 1:
                print('-' * int(vertical_lines - m) + ('-'.join(alpha[x + 1:number])[::-1]) + '-' +
                      ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - m))
                m += 2
                x -= 1
            else:
                print('-' * int(vertical_lines - m) +
                      ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - m))
                m += 2
                x -= 1
        elif i == number - 1:
            print('-' * int(vertical_lines - m) + ('-'.join(alpha[x + 1:number])[::-1]) + '-' +
                  ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - m))

        elif i > (number - 1):
            m -= 2
            x += 1
            if len(('-'.join(alpha[x:number]))) > 1:
                print('-' * int(vertical_lines - m) + ('-'.join(alpha[x + 1:number])[::-1]) + '-' +
                      ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - m))
            else:
                print('-' * int(vertical_lines - m) +
                      ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - m))


def sol_two():
    alpha = string.ascii_lowercase

    n = 5
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(L[:0:-1] + L))


res_1 = timeit.timeit(sol_one, number=10000)
res_2 = timeit.timeit(sol_two, number=10000)

print(res_1)
print(res_2)
