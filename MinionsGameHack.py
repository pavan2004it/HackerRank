

def minion_game(string):
    stuart_score = 0
    kevin_score = 0

    for i in range(len(string)):
        if string[i].startswith(('A', 'E', 'I', 'O', 'U')):
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)
    # kevin = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i: j] != ''
    #          if string[i: j].startswith(('A', 'E', 'I', 'O', 'U'))]
    # kevin = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i: j] != ''
    #          if string[i] in vowel]
    # kevin_score = len(kevin)
    #
    # stuart = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i: j] != ''
    #           if string[i] not in vowel]

    # stuart = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i: j] != ''
    #           if string[i: j].startswith(('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
    #                                       'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y'))]
    # stuart_score = len(stuart)

    if stuart_score > kevin_score:
        print("Stuart {0}".format(stuart_score))
    elif kevin_score > stuart_score:
        print("Kevin {0}".format(kevin_score))
    else:
        print("Draw")

# for i in range(len(s)):
#     for j in range(len(s) + 1):
#         print(s[i:j])


minion_game("")


# s = "BANANA"
# vowels = 'aeiou'
# for i in range(len(s)):
#     if s[i] in vowels.upper():
#         print(len(s) - i)
