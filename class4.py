'''
a=5
print(id(a))
b=a
print(id(a))
print(id(b))
print(a is b)
c=6
print(id(c))
print(a is not c)

name = "Yogendra"
print("Yog" in name)
print("yog" not in name)

print(5+2*3)'''

# apple
# unit price
# qty
# total
# discount
'''
Product = input("Enter any product name: ")
unitPrice = float(input("Enter the unit price of the product: "))
quantity = float(input("How much you want to buy: "))
total = unitPrice*quantity
print("your total value is:",total," before discount")
discount=int(input("your discount is: "))
finalPrice = total - (total*discount/100)
print("YOU HAVE TO PAY ",finalPrice)'''

a=5
b=6
print("value of a is",a,"and the value of b is",b)