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
    
    
# lists are like arrays. indexes work the same as with arrays
def lists():
    a = ["this", "is", "a", "list"]
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    print(m[1][2])
    
def things():
    things = ["text", 0, [1, 2, 8], 4.56]
    print(things[2][2])
    
    
# strings can be indexed too. spaces are a char so they have an index
def strings():
    str = "Hello World"
    print(str[6])
    
def testprint():
    x = "Python"
    print(x[1] + x[4])
    
def third_char():
    input = str(input())
    print(input[2])
    
def list_output():
    x = [2, 4]
    x = x * 3
    print(x[3])
    
def in_operator():
    # to check if item is in list, use `in` operator, returns bool
    nums = [10, 9, 8, 7, 6, 5]
    nums[0] = nums[1] - 5
    if 4 in nums:
        print(nums[3])
    else:
        print(nums[4])
    
def in_substring():
    # `in` can be used to see if a substring is part of a string
    x = "hello world"
    if "world" in x:
        print("Yes")
        
def not_in_list():
    nums = [1, 2, 3]
    print(not 4 in nums)    # true
    print(4 not in nums)    # true
    print(not 3 in nums)    # false
    print (3 not in nums)   # false
    
def for_loops():    
    string = "as;dlfknawroignaw[irgn"
    # this is like the `for ... in` loop in JS
    for letter in string: # defines a var that takes the value of each iteration
        print(letter)
        
def break_for():
    list = [2,3,4,5,6,7]
    for x in list:
        if (x % 2 == 1 and x > 4):
            print(x)
            break

# for loops - number of iterations is fixed.

# while loops - num of iterations isn't known, 
# especially if num depends on conditions 
# inside the body of the loop

def output_sum():
    x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
    sum = 0
    for i in x:
        sum += i
    print(sum)
    
def cont():
    nums = [1,2,3,4]
    res = 0
    for x in nums:
        if (x % 2 == 0):
            continue
        else:
            res += x
    print(res)
    
def ranges():
    # creates number sequences, default starts at 0, increments by 1 and ends at the number before specified num
    # to output as a list, must convert 
    nums = list(range(10))
    print(nums)
    
def test_range():
    nums = list(range(5)) # [0,1,2,3,4]
    print(nums[4])
    
def two_args():
    # range w one arg creates an obj w values from 0 to the num.
    # range w two args creats an obj w values from the 1st num to 2nd
    nums = list(range(3, 8)) # prints: [3,4,5,6,7]
    print(nums)
    
def range_test():
    print(range(20) == range(0, 20)) # True
    
def range_step():
    # 3rd arg for range(): sets interval of sequence

    numbers = list(range(5, 20, 2))
    print(numbers) # [5,7,9,11,13,15,17,19]

    neg = list(range(7, 3, -1))
    print(neg) # [7,6,5,4]
    
def for_range():
    for i in range(5):  # prints "hello" 5 times
        print("hello")
        
def date_picker():
    # output all years in a given period
    num1 = int(input())
    num2 = int(input())
    output = list(range(num1, num2))
    print(output)
   
    
    