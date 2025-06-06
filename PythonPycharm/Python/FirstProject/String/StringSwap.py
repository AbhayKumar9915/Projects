def SwapStr(str1, str2):
    print('Before swap str1 is {} and str2 is {}'.format(str1, str2))
    str1 = str1 + str2
    str2 = str1[0: len(str1) - len(str2)]
    str1 = str1[len(str2):]
    print('After swap str1 is {} and str2 is {}'.format(str1, str2))


SwapStr('Hello', 'Abhay')

