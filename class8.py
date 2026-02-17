'''
for i in range(1,6):
    print(i)
'''
'''
num = 1
while num<=5:
    print(num)
    # num=num+1
    num+=1
'''
'''
a=10
print(a)
a=a+2
print(a)
a=a+5
print(a)
a=a-2
print(a)
a=a-7
print(a)
a=a*2
print(a)
'''
''' 
pwd = ""
while pwd!="admin":
    pwd=input("Enter you password: ")
print("Now you can access the mail")
'''
'''
count =1
while count<=3:
    print(f"Attempt{count}")
    count+=1
'''
is_running = True
battery =100
while is_running:
    print(f"System is running... Battery: {battery}%" )
    battery-=20
    if battery <=0:
        is_running = False
print("system shutdown")

