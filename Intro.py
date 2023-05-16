'''Simple way to handle geting input and passing it'''
'''
user_input = input("Type something : ")
print(user_input)
'''
'getAge = input("Can you input your age:  ")'
'''Note the input function outputs to a string so you need to convert the string to an int'''
'new_age = (int(getAge)+50)'
'''Remember you will have to convert the int back to a string to print.'''
'print("In 50 years you will be "+str(new_age))'
'''To make a list its the same as a string however you use []'''

list = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
'''This will print the 0th element of the list'''
print(list[0])
list.append('Foxtrot')
list.append('Golf')
print(list)
'A tuple is like a lsit but not mutable, they cannnot be changed so methods to add or remove do not exist'
tuple = ('Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo')
print(tuple[0])
'A dictionary uses a key value pair arrangement'
'Every Value has a key with which you use to reference the value.'
dict = {'id': 0, 'Name': 'Ralph', 'Cities': ('PoS', 'Toronto', 'NY', 'Paris')}
print(dict['id'])
print(dict['Name'])
print(dict['Cities'])
'You can put a tuple within a dictionary and call a specific value in the tuple'
print(dict['Cities'][2])

a = 5
if a < 5:
    print('Foo')
elif a == 5:
    print('Foo-Bar')
else:
    print('Bar')
'A simple Function'


def mins_to_hrs(mins, secs):
    hrs = (mins / 60) + (secs / 3600)
    return hrs


print(mins_to_hrs(70, 300))
'''If you specify a default value then try to make the function such that
the specific parameter is passed first and then the default. 
So a function def function1(param1, param2=X) will pass X if X is not specified
'''


def simpleProg():
    age_In = int(input("Enter age : "))
    if age_In < 20:
        print("You're still young.")
    elif age_In <= 30:
        print("Still got it.")
    elif age_In <= 40:
        print("Kinda pushin' it.")
    else:
        print("Might as well drop.")


simpleProg()

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for item in array:
    print(item)
