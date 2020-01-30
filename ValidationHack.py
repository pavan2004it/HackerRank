s = input()

print(any(st.isalnum() for st in s))
print(any(st.isalpha() for st in s))
print(any(st.isdigit() for st in s))
print(any(st.islower() for st in s))
print(any(st.isupper() for st in s))

# if any(st.isalnum() for st in s):
#     print("True")
# else:
#     print("False")
#
# if any(st.isalpha() for st in s):
#     print("True")
# else:
#     print("False")
#
# if any(st.isdigit() for st in s):
#     print("True")
# else:
#     print("False")
#
# if any(st.islower() for st in s):
#     print("True")
# else:
#     print("False")
#
# if any(st.isupper() for st in s):
#     print("True")
# else:
#     print("False")
