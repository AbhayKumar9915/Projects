def HighestFreqChar(string):
    dct = {}
    for ch in string:
        if ch in dct:
            dct[ch] += 1
        else:
            dct[ch] = 1

    value = [i for i in dct if dct[i] == max(dct.values())]
    return value


print(HighestFreqChar('abhay'))
