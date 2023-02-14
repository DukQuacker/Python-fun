# Making a varable

first_name = "Zach"
last_name = "Breazile"
full_name = first_name + " " + last_name

print("hello " + full_name)
print(type(full_name))

age = 23
age += 1
print(age)
print(type(age))
print("Your age is: " + str(age)) #this will convert the age varable to a usable string varable

height = 250.5
print("Your height is: " + str(height) + "cm")
print(type(height))

human = False
print("Are you a human: " +str(human))
print(type(human))


#Multiple assignment

#new_name = "Zach"
#new_age = 23
#attractive = True

new_name, new_age, attractive = "Zach", 23, True

Zach = Sophia = 23

print(new_name)
print(new_age)
print(attractive)
print(Zach)
print(Sophia)

# String tools 

my_name = "zach"
print(len(my_name))
print(my_name.find("z"))
print(my_name.capitalize())
print(my_name.upper())
print(my_name.lower())
print(my_name.isdigit())
print(my_name.isalnum())
print(my_name.count("z"))
print(my_name.replace("z","n"))
print(my_name*3)


#Type casting

x = 1   #int
y = 2.0 #float
z = "3" #string

x = float(x)
z= int(z)

print(x)
print(int(y))
print(z*3)

