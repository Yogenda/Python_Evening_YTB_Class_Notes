'''
input = "ADmIn"

if input == "Admin" or input=="admin":
    print(input)
    
if input.lower() =="admin":
    print(input)

print(input.lower())
'''
'''
#strip(): cleaning user input
raw_input = "   admin_user    "
print(raw_input)
cleaned = ""
for char in raw_input:
    if char !=" ":
        cleaned +=char
print(cleaned)


clear = raw_input.strip()
print(clear)
'''

# split() join() : data transformation
'''
word=["python","is","easy"]
sentence =""
for w in word:
    sentence+=w+" "
print(sentence)

sen = " ".join(word)
print(sen)
'''

#replace(): Data redaction/ sanitization
'''
text = "Error in system"
print(text)
temp_list = list(text)
temp_list[0:5] ="Falut"
text="".join(temp_list)
print(text)

text = text.replace("Falut","Faultyyyy")
print(text)  
'''

#find() and index(): substring location
'''
log = "2026-02-24: Access Denied"
for i in range(len(log)):
    if log[i:i+6]=="Denied":
        pos = i
print(pos)

pop = log.find("Denied") #boyer-moore and horspool
print(pop)
'''
#count(): frequency analysis
'''
DNA = "ADFKSLDJFLLAFAASJDFLKJALDFJLSKJFLKASJDFKLJSDFLKA"
count_A = 0
for char in DNA:
    if char =="A":
        count_A+=1
print(count_A)

count_A=DNA.count("A")
print(count_A)
'''




