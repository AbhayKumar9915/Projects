# Counting number of word in string and printing all value in key-value format by adding in dict
# Algorithm
# - Split all words and store in list
# - Take an empty dict
# - Transverse to each char of word
# - Take value of count 0, and increase by 1 in each iteration
def NumberOfCharInEachWordInString(string):
    splString = string.split()
    d = {}
    for word in splString:
        count = 0
        for ch in word:
            count = count + 1
            d[word] = count
    return d


# Counting each and every character in string
def TotalCountOfChar(string):
    c = 0
    for i in string:
        if i == ' ':
            pass
        else:
            c = c + 1
    return c


# Count occurrence of each character in string
def OccurrenceOfEachCharInString(string):
    dct = {}
    for ch in string:
        if ch == ' ':
            pass
        elif ch in dct:
            dct[ch] += 1
        else:
            dct[ch] = 1
    return dct


String = 'I Love Python Programming'
print(NumberOfCharInEachWordInString(String))
print(TotalCountOfChar(String))
print(OccurrenceOfEachCharInString(String))
