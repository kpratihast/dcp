def firstRecur(s):
    indiv = []
    found = 0
    for char in list(s):
        if not found:
            if char not in indiv:
                indiv.append(char)
                found = 0
            else:
                found = 1
                return print(char)
    if not found:
        return print("Not found")


firstRecur("aabbcca")
