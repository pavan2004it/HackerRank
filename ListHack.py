num_list = []

commands = int(input())

for _ in range(commands):
    command, *nums = input().split()
    nums = [int(i) for i in nums]
    if command.lower() == "insert":
        num_list.insert(nums[0], nums[1])
    elif command.lower() == "print":
        print(num_list)
    elif command.lower() == "remove":
        num_list.remove(nums[0])
    elif command.lower() == "append":
        num_list.append(nums[0])
    elif command.lower() == "pop":
        num_list.pop()
    elif command.lower() == "reverse":
        num_list.reverse()
    elif command.lower() == "sort":
        num_list.sort()
