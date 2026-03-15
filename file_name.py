#Задание 1
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