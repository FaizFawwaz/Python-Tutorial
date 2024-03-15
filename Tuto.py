integers = [1,2,3,4,5]
for number in integers:
    print(number)  
    
integers = [1,2,3,4,5]    
for Jelly in integers:
    print(Jelly + Jelly)
    
    
    
ice_cream_dict = {'name': 'Faiz', 'weekly intakes':5, 'week favorite ice cream': ['mcc', 'chocolate']}
for cream in ice_cream_dict.values():
    print(cream)
for key, value in ice_cream_dict.items():
    print(key, '->', value)   
    

flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Hot Fudge', 'Oreo', 'Marshmallow']
for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)
        

number = 0
while number < 5:
    print(number)
    number = number + 1
    
number = 1
while number < 10:
    print(number)
    number = number + 1
    
number = 0
while number < 5:
    print(number)
    if number ==3:
        break
    number = number + 1
    
number = 0
while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:
    print('No Longer < 5')
    
number = 0
while number < 5:
    number = number + 1
    if number == 3:
        continue
    print(number)  
else:
    print('No Longer < 5')
    
def first_func():
    print('We did it')
first_func()


def number_squared(number):
    print(number**2)
number_squared(5)

def number_squared_cust(number,power):
    print(number**power) 
number_squared_cust(5,3) 

def number_args(*number):
    print(number[0]*number[1])
number_args(5,6,1,2,8)



args_tuple = (5,6,1,2,8)

def number_args(*number):
    print(number[0]*number[1])
number_args(*args_tuple)

def number_squared_cust(number,power):
    print(number**power)
number_squared_cust(power = 5,number=3)

def number_kwarg(**number):
    print('My number is:' + number['integer'])
number_kwarg(integer = '2309') 

def number_kwarg(**number):
    print('My number is:' + number['integer'] + ' ' + 'My other number:' + number['integer2'])
number_kwarg(integer = '2309', integer2 = '1234') 

num_int = 7
type(num_int)

num_str = '7'
type(num_str)

num_str_conv = int(num_str)
num_sum = num_int + num_str_conv
print(num_sum)

dict_type = {'name': 'Faiz', 'age': 28, 'hair': 'N/A'}
dict_type.items()
dict_type.values()
dict_type.keys()
list(dict_type.keys())

x = 3
print(x)
