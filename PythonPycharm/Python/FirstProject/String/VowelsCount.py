#Count each vowels in string

def countvowels(st):
    vowels='aeiou'
    count = 0
    for ch in st:
        if ch in vowels:
            count += 1
    return count

print(countvowels('i love python programming'))


#Count number of each vowel in string

def each_vowel(st2):
    d = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for ch in st2:
        if ch in d:
            d[ch] += 1
    return d

print(each_vowel('i love python programming'))