# With For Loop
def RevStringFor(string):
    str2 = ""
    for ch in string:
        str2 = ch + str2
    return str2


# With While Loop:
def RevStringWhile(string1):
    revstr = ""
    i = (len(string1))
    while i > 0:
        revstr += string1[i - 1]
        i = i - 1
    return revstr


# With Recursion:
def RevStringRecursion(string2):
    if len(string2) == 0:
        return string2
    else:
        return RevStringRecursion(string2[1:]) + string2[0]


string3 = 'Abhay'
print(RevStringFor(string3))
print(RevStringWhile(string3))
print(RevStringRecursion(string3))




