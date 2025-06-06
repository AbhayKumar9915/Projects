def div(a):
    i = 50
    print(i/a)

def list1():
    try:
        a = [5, 6, 8, 1]
        print(a[4])
    except Exception as e:
        print(e)

def read():
    try:
        with open('Test.txt', 'r') as file:
            Text = file.read()
            print(Text)
    except Exception as e:
        print(e)
    finally:
        print('Finally Execute everytime irrespective of Fail or Pass')

def zero_div(a):
    i = 10
    try:
        print(i/a)
    except Exception as e:
        print(e)


div(5)
list1()
div(10)
read()
div(2)
zero_div(0)

