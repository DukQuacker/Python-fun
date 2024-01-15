#print("hello, world!") #print functions for hello, world!

Name = input("What's your name? ")

#example of using end from the python documention to replace the space in the print function.
#print("hello,", end = " ") 
#print(Name)

#removing white space from str
Name = Name.strip().title()

#Capitalize the name of the user
#Name = Name.capitalize()

#Name = Name.title()

print(f"hello, {Name}")

