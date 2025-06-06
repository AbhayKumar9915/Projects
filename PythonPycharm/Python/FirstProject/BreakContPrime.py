print('*******Break*********')
i = 0
while i < 5:
    if i == 3:
        i = i+1
        break
    print(i)
    i = i + 1

print('*******Continue*********')
j = 0
while j < 5:
    if j == 3:
        j = j + 1
        continue
    print(j)
    j = j + 1

print('*******Prime*********')
n = int(input('Enter the Number: '))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print('Not Prime')
            print('{} is divisible by {}'.format(n, i))
            break
    else:
        print('Prime')

print('*******Prime in range of 100*********')
def prime_num():
    lst = []
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)
prime_num()
