# sololearn 12/28/22

def example1():
    a = 2
    b = 4
    print(a + b)
    print("42" + "5")

# distance = 7425 miles, speed = 550 mph
# print out total time in hours (float)
def flight_time():
    distance = 7425
    speed = 550
    time = float(distance / speed)
    print(time)

# 12/29/22

# input() always returns a string
def input_x():
    x = input()
    print(x)

def input_num():
    number = input()
    print("You entered: " + number)

def name_age():
    name = input()
    age = input()
    print(name + " is " + age + " years old")

def input_int():
    age = int(input())
    print(age)

def casting_ints():
    x = "2"
    y = "4"
    z = int(x) + int(y)
    print(z)

def cast_float():
    height = float(input())
    print(height)

def cast_str():
    age = 42
    print("Age is " + str(age))

def input_ints_sum():
    x = int(input())
    y = int(input())
    print(x + y)

def repeat_str():
    x = str(input())
    y = int(input())
    print(x * y)
    
def print_area():
    width = input()
    height = input()
    area = int(width) * int(height)
    print(area // 9)
    
