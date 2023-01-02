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
    
def in_place():
    x = 2
    print(x)
    x += 3
    print(x)
    
def operators():
    x = 9
    x %= 2
    x += 3
    print(x)
    
def miles_to_km():
    miles = int(input())
    km = miles * 1.60934
    print(km)
    
def country_cards():
    country = str(input())
    capital = str(input())
    print(
        "Country: " + country + "\nCapital: " + capital 
    )

def chess_scores():
    wins = int(input())
    ties = int(input())
    points = wins + (ties * 0.5)
    print(points)
    
    
def bank_withdrawal():
    balance = int(input())
    withdrawal = int(input())
    print("Your balance: " + str(balance - withdrawal))
    
def idk():
    spam = "7"
    spam = spam + "0"
    eggs = int(spam) + 3
    print(float(eggs))
    
def modulo():
    x = 3
    num = 17
    print(num % x)
    
def tip_calc():
    bill = int(input())
    tip = float(bill * 0.2)
    print(tip)
    
def booleans():
    print(2 == 3)
    print("hello" == "hello")
    x = 7
    print(x != 8)
    print(x > 5)
    print(x >= 7)
    print('a' > 'b')
    print("Bob" > "Dave")
    
    y = (7 > 5)
    print(int(y))
    
def tru():
    print(7 != 8)
    
def if_stmt():
    x = 42
    if x > 5:
        print("x > 5")
        
    num = 12
    if num > 5:
        print("Bigger than 5")
        if num <= 47:
            print("between 5 and 47")
            
def long_if():
    num = 7
    if num > 3:
        print("3")
        if (num < 5):
            print("5")
            if num == 7:
                print("7")
                
def water_boiling():
    temp = int(input())
    if temp > 100:
        print("Boiling")
        
def abc():
    x = 'a'
    if (x < 'c'):
        x += 'b'
    if (x > 'z'):
        x += 'c'
        
    print(x)

def kindle():
    age = int(input())
    if age <= 19:
        print("Take your kindle!")
        
def else_stmt():
    x = 4
    if x == 5:
        print("yes")
    else:
        print("no")
        
def nested_ifs():
    if 1 + 1 == 2:
        if 2 * 2 == 8:
            print("if")
        else:
            print("else")
        
def elif_stmt():
    num = 3
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    else:
        print("else")
        
def check_age():
    age = int(input())
    if age >= 18:
        print("Allowed")
    else:
        print("Sorry")
        
def bool_operators():
    print(1 == 1 and 2 == 2) # True
    print(1 != 1 and 2 > 3) # False
    
    print( 2 < 1 or 3 > 6 ) # False
    
    print(not 1 == 1) # False
    print(not 1 > 7) # True
    
def if_not_true():
    if not True:
        print("1")
    elif not (1 + 1 == 3):
        print("2")
    else:
        print("3")
        
def multiple_conditions():
    country = "US"
    age = 42
    if (country == "US" or country == "GB") and (age > 0 and age < 100):
        print("Cool")
      
      
def cond():
    hour = 9
    day = 23
    print((hour > 12 and day <= 15) or (hour < 10))
    
def age_groups():
    age = int(input())
    if (0 < age <= 11):
        print("Child")
    elif (12 <= age <= 17):
        print("Teen")
    elif (18 <= age <= 64):
        print("Adult")
    else:
        print("out of bounds")
        
def while_loops():
    i = 1
    while i <= 5:
        print(i)
        i += 1
    print("finished")

def how_many_nums():
    i = 1
    while i <= 5:
        print(i)
        i += 1
        
# first commit of 2023

def if_while():
    x = 1
    while x < 10:
        if x % 2 == 0:
            print(str(x) + " is even")
        else:
            print(str(x) + " id odd")
            
        x += 1

def print_even():
    x = 0
    while x <= 20:
        if (x % 2 == 0):
            print(x)
        x += 1
        
def breaks():
    i = 0
    while True:
        print(i)
        i += 1
        if i >= 5:
            print("Breaking")
            break
    
    print("finished")

def continues():
    i = 0
    while i < 5:
        i += 1
        if i == 3:
            print("Skipping 3")
            continue
        print(i)
        
def while_true():
    i = 0
    while True:
        i += 1
        if (i == 2):
            continue
        if (i == 5):
            break
        
        print(i)
        
def ticketing():
    price = 100
    total = 0
    pass1 = int(input())
    pass2 = int(input())
    pass3 = int(input())
    pass4 = int(input())
    pass5 = int(input())
    if pass1 > 3:
        total += price
    if pass2 > 3:
        total += price
    if pass3 > 3:
        total += price
    if pass4 > 3:
        total += price
    if pass5 > 3:
        total += price
        
    print(total)
    
ticketing()