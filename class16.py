'''nums=[1,2,3]
print(nums)
print(type(nums))

num = list((1,2,3))
print(num)
print(type(num))

newList = list(range(1,11))
print(newList)
print(type(newList))

square = [x*x for x in range(6)]
print(square)
print(type(square))'''
#clean, faster, preferred in interview
number = [10,20,30,40,50,60]
print(number[2])
print(number[-1])
#number[start:end:step]
print(number[1:3])
print(number[3:5])
print(number[:4])
print(number[3:])
print(number[::1])
print(number[::2])
print(number[1:4:2])
print(number[::-1])
number[0]=100
print(number)
del number[1]
print(number)