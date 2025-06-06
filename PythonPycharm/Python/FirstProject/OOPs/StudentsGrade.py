class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi ', self.name)
        print('Your Marks are:', self.marks)

    def grade(self):
        if self.marks > 75:
            print('First Grade')
        elif 60 <= self.marks <= 75:
            print('Second Grade')
        elif 35 <= self.marks <= 60:
            print('Third Grade')
        else:
            print('Failed')


n = int(input('Enter no of Student:'))
for i in range(n):
    name = input("Enter Student's Name:")
    marks = int(input('Enter Marks:'))
    s = Student(name, marks)
    s.display()
    s.grade()
    print('*'*20)
