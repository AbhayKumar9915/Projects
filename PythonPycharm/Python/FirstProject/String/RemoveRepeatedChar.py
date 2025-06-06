def RemoveRepChar(string):
    string1 = ''
    for ch in string:
        if ch in string1:
            pass
        else:
            string1 = string1 + ch
    return string1


print(RemoveRepChar('abhayabysdaeh'))
