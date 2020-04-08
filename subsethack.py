number_of_tests = int(input())

for _ in range(number_of_tests):
    set_a_elements = int(input())
    set_a = {x for x in input().split()}
    set_b_elements = int(input())
    set_b = {x for x in input().split()}

    print(set_a.issubset(set_b))
