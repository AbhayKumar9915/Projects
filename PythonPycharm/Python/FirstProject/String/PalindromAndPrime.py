string = input('Enter value to check: ')
if string == str[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

a = int(input('Enter Num to check: '))
if a > 1:
    for x in range(2, a):
        if (a % x) == 0:
            print('Not Prime')
            break
    else:
        print('Prime')
else:
    print('Not Prime')
