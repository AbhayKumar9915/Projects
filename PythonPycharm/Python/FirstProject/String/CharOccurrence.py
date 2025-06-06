def countChar(string):
    count = 0
    char = input('Enter char: ')
    for ch in string:
        if char == ch:
            count += 1
        else:
            pass
    print("Occurrence of '{}' in given string is {}".format(char, count))


countChar('i love python')
