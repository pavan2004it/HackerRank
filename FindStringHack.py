import re


def count_substring(string, sub_string):
    return len(re.findall('(?={0})'.format(sub_string), string))


if __name__ == "__main__":
    string_new = input().strip()
    sub_string_new = input().strip()
    count = count_substring(string_new, sub_string_new)
    print(count)

