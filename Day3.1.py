#2/6/2024 I'll be going over loops via CS50

#i = 3
#while i != 0:
 #   print("meow")
 #   i -= 1      #This works like c++'s ++ or -- because python can't do that

#for i in range(3): #You can change i to an _ which just means do this without meaning you're not going to be using this varable in future code
 #   print("meow")

#while True: #used to make an infinite loop
#    n = int(input("What's n? "))
#    if n > 0:
#        break #break out of the loop when the if is met

#for _ in range (n):
#    print("meow")
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n "))
        if n > 0:
            return n #this could be replaced by break but this should break the loop too

def meow(n):
    for _ in range(n):
        print("meow")

main()
"""
"""
students = ["Hermione", "Harry", "Ron", "Draco"]


for student in students:
    print(student)

for i in range(len(students)): #If you need to iterate via a number but have a list do this
    print(i + 1, students[i])
"""
'''
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor", 
            "Ron": "Gryffinor",
            "Draco": "Slytherin"
            }   #Makeing a dictionary
for student in students:
    print(student , students[student], sep=", ")
'''
students = [ #dictionary list
        {"Name" : "Zach", "House" : "Tech", "Major" : "CS"}, 
        {"Name" : "Noah", "House" : "Parent's", "Major" : None},
        {"Name" : "Jacob", "House" : "Milne", "Major" : "History"},
        {"Name" : "Robot", "House" : "Tech", "Major" : "Everything"}
        ]

for student in students:
    print(student["Name"],student["House"],student["Major"])