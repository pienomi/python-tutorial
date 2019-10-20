# Update your contetns here
# https://www.tutorialspoint.com/python/python_strings.html

# Lines and Indentation
if True:
    print("True")
else:
    print("False")

# Multi-line
total = item_one + \
        item_two + \
        item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# Quotation
word = 'word'
sentence = "This is a sentence"
paragraph = """This is paragraph.
    hello world~~"""

# Waiting for user
raw_input("\n\nPress enter to exit")

# Multiple Statesment on a single line
import sys; x = 'foo'; sys.stdout.write(x + '\n')

# Multiple assignment
a = b = c = 1;
a, b, c = 1, 2, "john"

# List
list = ['sophie', 'dophie', 'hophie']
list_again = ['hoho']

print(list[1:3]) # ['dophie', 'hophie']
print(list[2:]) # ['hophie']

print(list_again * 2) # ['hoho', 'hoho']
print(list + list_again) # concatenated result

# Tuple - tuple is read only in python
tuple = ('sophie', 'dophie', 'hophie')
tuple_again = ('hoho')

print(tuple_again * 2) # ('hoho', 'hoho')
print(tuple + tuple_again) # concatenated result

# ... so this is possible for list
list[0] = 'sssophie'

# ... but this is not possible for tuple
tuple[0] = 'sssophie' # invalid syntax

# Dictionary -  key-value pairs
dict = {}
dict['a'] = 'a'
dict[2] = 'two'

dict.keys() # 'a', 2
dict.values() # 'a', 'two'

# Arithmetic operators

a = 1
b = 2

print(a + b, a * b, a - b, a / b)
print(a % b) # modulus
print(a ** b) # exponential

# Comparison operators
# Assignment operators
# Bitwise operators
# Logical operators
# Membership operators - not in, in
# Identity operators = is, is not


# Conditional statement
number = 0

if number:
    print('This is truthy value')
else:
    print('This is falsy value')

# this would be 'else' because python consider 0 or null as falsy value

# Loop
while number < 10:
    print('Still number is under 10')
    number += 1

for name in list:
    if (name == 'sophie'):
        print('this is sophie')
    else:
        print('the name is' + name)

# ... you can use iterated number using len()

for index in range(len(list)):
    print(list[index])

# can write nested loop as well

# Loop control statement
## break: terminate the loop and go to next
## continue: skip current condition test
## pass: nothing to do but just write for the syntax

# String special operators

a = 'hello'
b = 'sophie'

# a + b = 'hellosophie'
# a * 2 = 'hellohello'
# a[1] = 'e'
# a[1:4] = 'ell'
# h in a = True
# h not in a = False

# I'm using python 2 unfortunately but will follow python 3
print "my name is %s and i am %d years old" % ('sophie', 11)


class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__== '__main__':

    my_car = Car()
    print("I'm a car")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know what to do")
            continue
        if action == "A":
            my_car.accelerate()
        elif action == "B":
            my_car.brake()
        elif action == "O":
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == "S":
            print("This car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()