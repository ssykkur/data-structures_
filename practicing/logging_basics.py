import logging 

#5 standart levels: 1.debug 2.info 3.warning 4.error 5.critical
# 1.detailed information, typically of interested only when diagnosing problems 
# 2.confirmation that things are working as expected 
# 3.an indication that somehting unexpected happened or indicative of some problem in the near future. the software is still working as expected
# 4.due to a more serious error the software has not been able to perform some function
# 5.a serious error, indicating that the program itself may be unable to continue running 
# By default only warning and above will be logged 

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y

def add(x, y):
    return x - y

def add(x, y):
    return x * y

def add(x, y):
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug(f'add: {num_1} + {num_2} = {add_result}')


something = ['opo', 'oro ']

for count, value in enumerate(something):
    print(count, value)