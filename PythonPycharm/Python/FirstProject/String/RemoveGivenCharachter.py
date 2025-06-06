def RemChar(string):
    char = input('Enter the char to remove: ')
    string1 = ''
    if char in string:
        for ch in string:
            if char == ch:
                pass
            else:
                string1 = string1 + ch
    else:
        print('Char not in string')
    return string1


print(RemChar('testing'))
