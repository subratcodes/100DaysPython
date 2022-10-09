def isogram(s):
    if (len(s) == 0): return 0
    map = {}
    for x in range(0, len(s)):
        if (s[x] in map):
            return 0
        else:
            map[s[x]] = 1
    return 1


def print_first_letter(String):
    if (len(String) == 0): return -1
    result = ''

    for x in range(0, len(String)):
        if (x == 0): result += String[x]
        elif (String[x].isspace()):
            result += String[x+1]
    return result



  