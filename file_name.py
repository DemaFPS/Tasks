#Задание 1
""""
s = "Hello, World!"
print(s[0])
print(s[-1])
print(s[7:-1])

#Задание 2
str = input()
if len(str) %2 == 0:
    print(str.upper())
else:
    print(str.lower())

#Задание 3
str = input()
count=0
for i in str:
    if i in "aeiouAEIOU":
        count+=1
print(count)

#Задание 4
str = input()
rez=""
for i in range(len(str)):
    if i==0 or str[i] != str[i-1]:
        rez+=str[i]
print(rez)
"""
#Задание 5
str1=input()
str2=input()
c=0
if len(str1) != len(str2):
    print("False")
for i in str1:
    if i in str2:
        c+=1
if c!=0:
    print("False")
else:
    print("True")