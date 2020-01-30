s = "Www.HackerRank.com"
new_s = ""
for element in s:
    if element.islower():
        new_s += element.upper()
    elif element.isupper():
        new_s += element.lower()
    else:
        new_s += element


print(new_s)


