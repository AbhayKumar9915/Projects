"""An anagram is a word or phrase formed by rearranging
the letters of a different word or phrase"""
def anagram(str1, str2):
    if len(str1) != len(str2):
        print("Can't be Anagram")
    else:
        str1 = str1.lower()
        str2 = str2.lower()

        string1 = list(str1)
        string2 = list(str2)

        string1.sort()
        string2.sort()

        if string1 == string2:
            print('Its Anagram')
        else:
            print('Not an Anagram')

anagram('secure', 'Rescue')
anagram('abhay', 'abhay1')
anagram('Eleven plus two', 'twelve plus one')
anagram('Jade', 'Jane')


def pangram(st):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    st=st.lower()
    for i in alphabet:
        if i not in st:
            return 'Not Pangram'
    return 'Pangram'

print(pangram('The quick brown fox jumps over the lazy dog'))

