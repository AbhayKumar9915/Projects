str1 = 'Abhay'
str2 ='bhaya'

str1 = str1.lower()
str2 = str2.lower()

if(len(str1)!= len(str2)):
    print("Can/'t be Anagram")
else:
    string1 = list(str1)
    string1.sort()
    string2 = list(str2)
    string2.sort()
    if(string1 == string2):
        print('Anagram')
    else:
        print('Not Anagram')
