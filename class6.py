'''
age = 13
if age>=18:
    status ="Adult"
else:
    status="Minor"
print(f"You are: {status}")
'''
'''
age = 19
status = "Adult" if age>=18 else "Minor"
print(f"You are: {status}")
'''
'''
user_exist = False
password_corret = True
 
if user_exist:
    if password_corret:
        print("you log in")
    else:
        print("no log in")
else:
    print("no user")
'''
'''
if user_exist and password_corret:
    print("you log in")
'''
#leap year checker
'''year = int(input("Enter your year: "))
if (year%4==0 and year %100!=0)or(year %400==0):
    print("leap year")
else:
    print("not a leap year")'''

#nested membership check
'''age = int(input("Enter your age: "))
has_ticket = False
is_vip = False
if age>=18:
    if is_vip or has_ticket:
        print("Access granted")
    else:
        print("Please buy a ticket")
else:
    print("Too young to enter")
'''
'''
bmi = int(input("Enter your bmi: "))
if bmi <18.5:
    status="underweight"
elif 18.5 <= bmi <25:
    status="Normal weight"
elif 25<=bmi <30:
    status="overweight"
else:
    status="obese"
print(f"Status: {status}")
'''

#fizzBuzz
num = int(input("Enter any number: "))
if num %3 ==0 and num%5==0:
    print("FizzBuzz")
elif num%3 ==0:
    print("Fizz")
elif num%5 ==0:
    print("Buzz")
else:
    print(num)

