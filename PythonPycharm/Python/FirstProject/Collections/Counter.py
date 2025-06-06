# A Counter is a subclass of Dict
from collections import Counter


def StrCount(string):
    return Counter(string)


print(StrCount('abhay verma'))


c = Counter('aahashadbahdhadbah')
print(c)
print(c.items())
print(c.keys())
print(c.values())
print(c.pop('a'))
print(c)
# Similarly Clear(), Update and other methods can be used with Counter
