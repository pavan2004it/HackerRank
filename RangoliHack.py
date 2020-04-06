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

number = int(input())
M: int = 1
x = number - 1
vertical_lines = number + (number - 1)
alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]

for i in range(vertical_lines):
    if number == 1:
        print(alpha[number-1])

    elif x > 0 and i < (number - 1):
        if len(('-'.join(alpha[x:number]))) > 1:
            print('-' * int(vertical_lines - M) + ('-'.join(alpha[x + 1:number])[::-1]) + '-' +
                  ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - M))
            M += 2
            x -= 1
        else:
            print('-' * int(vertical_lines - M) +
                  ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - M))
            M += 2
            x -= 1
    elif i == number - 1:
        print('-' * int(vertical_lines - M) + ('-'.join(alpha[x + 1:number])[::-1]) + '-' +
              ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - M))

    elif i > (number - 1):
        M -= 2
        x += 1
        if len(('-'.join(alpha[x:number]))) > 1:
            print('-' * int(vertical_lines - M) + ('-'.join(alpha[x + 1:number])[::-1]) + '-' +
                  ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - M))
        else:
            print('-' * int(vertical_lines - M) +
                  ('-'.join(alpha[x:number])) + '-' * int(vertical_lines - M))


