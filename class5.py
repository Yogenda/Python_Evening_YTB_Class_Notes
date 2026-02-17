'''battery = int(input("Enter the battery percentage: "))
if battery<20:
    print("Warning :Low battery please charge")'''
'''
age = int(input("Enter your age: "))
if age>=18:
    print("you can vote")
else:
    print("you can not vote")'''
    
# write a program in python to check where a person can drive a car or not. and the age should be taken from use. if age is greate than 18 years he /she can drive.
'''
age = int(input("enter your age"))
if age>18:
    print("you can drive")
else:
    print("no you can not drive and you have to wait",18-age,"years")
'''
'''
score = int(input("Enter your marks: "))
if score>=90:
    print("Grade: A")
elif score >=70:
    print("Grade: B")
elif score >=50:
    print("Grade: C")
else:
    print("You are fail try again")
    '''
'''
if out_condi:
    #this out cond exec.
    if innercond
        #inner condtion exec
    else:
        #this will run if out condi is true but inner cond is false
'''
temp=31
is_night=False
motion_detection = True

if temp>30:
    action = "Turning on the AC"
elif temp<15:
    action = "Turning on the Heater"
else:
    action = "Temperature is optimized"

if is_night:
    if motion_detection:
        security_satus = "Alarm! motion detected"
    else:
        security_satus = "Night mode activated"
else:
    security_satus = "Day Mode activated"
print(f"Home Status: {action}")
print(f"Security Report: {security_satus}")
