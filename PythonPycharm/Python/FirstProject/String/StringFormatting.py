name = 'Abhay'
age = 28.55464545

print('***%formatting***')
# s = String,d = int, f = float
# %r and repr() deliver the string representation of the object, including quotation marks and any escape characters
# \t = tab,\n = new line
print('My name is %s and my age is %d' % (name, age))
print('My name is %r and my age is %d' % (name, age))
print('My name is %s and \t tab entered and my age is %f' % (name, age))
# .4f stands for how many numbers to show past the decimal point
print('My name is %r and\nnew line entered and my age is %0.3f' % (name, age))
# 10 would be the minimum number of characters the string should contain; these may be padded with whitespace
print('My name is %s and my age is %10.4f' % (name, age))

print('\n\n***.format()***')
# .format()
print('My name is {} and my age is {}'.format(name, age))
# with padding and decimal precision
print('My name is {0} and my age is {1:0.3f}'.format(name, age))
print('My name is {0} and my age is {1:10.3f}'.format(name, age))

print('\n\n***Alignment Padding and Precision***')
# left centre and right alignment with .format()
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Centre', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(10, 11, 12))
# Without alignment,int aligned right side by default
print('{0:8} | {1:8} | {2:8}'.format(10, 11, 12))
# String aligned left side by default
print('{0:8} | {1:8} | {2:8}'.format('Abhay', 'Adarsh', 'Ravi'))
