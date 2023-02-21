#User inputs
""" name = input("what is your name?: ") 
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
age = age +1
print("Hello "+name)
print("You are " +str(age)+ " yours old")
print("You are " + str(height)+"cm tall") """

#numbers

import math

""" pi = -3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))
print(min(x,y,z)) """

#string slicing

""" name = "Zach Breazile"

first_name = name[:4]
last_name = name[5:]
funky_name = name[0:13:2] #every 2 leter is output
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice]) """

age = int(input("How old are you?: "))


if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")