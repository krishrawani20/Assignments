# 01) Write a Python program to remove a specific key from a dictionary, retrieve all key
#value pair s, and check whether a given key exists.
'''car = {"brand": "Toyato",
       "model": "Carmry",
       "year": 2022,
       "color": "blue"}
print("Original dict: ",car )
a = input("Enter the key: ")
if a in car:
    car.pop(a)
    print("After removing key: ", car)
else:
    print("Key no exist.")


for k,v in car.items():
    print(k, ":", v) 

search = input("Enter the key for search: ")

if search in car:
    print("Key presents")
else:
    print("key not found")

#Write a Python program to create a dictionary by mapping two equal length lists, one
#containing keys and the other containi ng values.
keys = ["name", "age", "city"]
values = ["Krish", 20, "Dhanbad"]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Dictionary =", d)

#03 ) Write a Python program to verify whether a specific value is present anywhere in a dictionary.
roles = {"alice": "admin", "bob": "editor", "carol": "vi ewer"}
search = input("Enter the name: ")

if search in roles:
    print("editor and manager is present")
else:
    print("Not present")

#04) Write a Python program to create a new dictionary containing only a specified subset
#of keys from an existing dictionary.
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com",
"password": "s3cr3t", "joined": "2021 03 15"}

keys = ["id", "username", "email"]

new_dic = {}
for k in keys:
    if k in user:
        new_dic[k] = user[k]
print(k)

#5) Write a Python program to count how many times each character appears in a given
#string, storing the result s in a dictionary.
text = input("Enter th text: ")
dic = {}
for i in text:
     if i in dic:
        dic[i] = dic[i] + 1
     else:
        dic[i] = 1
print(dic)

#6) Write a Python program to find the key associated with the highest numerical value in a dictionary.
scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
max_score = max(scores.values())

for name in scores:
    if scores[name] == max_score:
        print(name, ":", max_score)

#7) Write a program in python that accepts a string from user and apply : len(s), upper(),
#lower(), title(), capitalize() functions on it.
text = input("Enter the text: ")
a = len(text)
b = text.upper()
c = text.lower()
d = text.title()
e = text.capitalize()
print(a)
print(b)
print(c)
print(d)
print(e)

#8) Write a program in P ython that accepts a string from user which has words separated
#by hyphen( hyphen(--). Use function list to split it based on hyphen(-)
s = input("Enter a hyphen-separated string: ")

words = s.split("-")

print("List of words:", words)

#9) W rite a Python program which reads a string from a user, prints the frequency of
#occurrence of first character and change all the occurrences of first character to ‘$’.
s = input("Enter the string: ")
first = s[0]

count= 0
for ch in s:
    if ch == first:
        count += 1
new_s = ""
for ch in s:
    if ch == first:
        new_s += "$"
    else:
        new_s += ch
print(count)
print(new_s)

'''
#10 )Write a program in Python whi ch takes a new string as input and prints the frequency
#of occurrence of first character in a string without using count function.

s = input("Enter the string: ")
si = s[0]
count = 0
for i in s:
    if i == si:
        count += 1
    else: 
        count == 0
print(si, ":", count)


#11) WAP in Python to read a string from user and print in it sorted order of words.
s = input("Enter the string: ")
for i in s:
    i = ord(i, reversed = True)
    
    
    print(i)
    