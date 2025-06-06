# Generator performance is better than other iterator
import random
import time

names = ['Abhay', 'Ravi', 'Adarsh', 'Ruchi']
subjects = ['Python', 'Java', 'Angular', 'HTML']


def people_list(num):
    result = []
    for i in range(num):
        persons = {'ID': i+1, 'Name': random.choice(names), 'Subject': random.choice(subjects)}
        result.append(persons)
    return result


t1 = time.process_time()
people = people_list(1000000)
t2 = time.process_time()
print('Time taken in list iterator: ', t2-t1)


def people_generator(num):
    for i in range(num):
        persons = {'ID': i+1, 'Name': random.choice(names), 'Subject': random.choice(subjects)}
        yield persons


t3 = time.process_time()
people = people_generator(1000000)
t4 = time.process_time()
print('Time taken in Generator: ', t4-t3)
