'''
text = "  Python  "
print(text.lower())
print(text.upper())
print(text.strip())
text = "Python*is*very-easy"
word = text.split("*")
print(word)
print(word[0])
word = ['Python', 'is', 'very-easy']
sentence = " ".join(word)
print(sentence)
text = "I love java"
print(text.replace("java","Python"))
text = "python"
print(text.find("z"))
text = "banana"
print(text.count("a"))

text = "Python"
# text[0]="j"
# print(text)
new_text = "j"+text[1:]
print(new_text)
'''
'''
result = ""
for i in range(1000):
    result+="a"
print(result)
'''
''' 
result = []
for i in range(1000):
    result.append("a")
final_string = "".join(result)
print(final_string)
'''
'''
a =[1,2,3]
a.append(5)
print(a)
'''
word = "madam"
if word == word[::-1]:
    print("palandrom")
else:
    print("Not a palandrom")
    



