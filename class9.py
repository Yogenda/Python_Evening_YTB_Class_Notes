'''
for i in range(1,10):
    if i==5:
        break
    print(i)
'''
'''
for i in range(1,6):
    if i==3:
        continue
    print(i)
'''
'''
for i in range(5):
    pass
'''
'''
# process even numbers, skip odds, stop if we hit an negative number
numbers=[2,3,4,7,8,10,-1,12,11]
for num in numbers:
    if num<0:
        print("We got a negative number so we can break")
        break
    if num%2!=0:
        continue #skip the odd number
    print(f"processing even numbers: {num}")
'''


