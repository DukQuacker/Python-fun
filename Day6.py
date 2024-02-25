#Doing File i/o CS50 Zachary Breazile 2/25/24
"""
name = input("What's your name? ")

with open("names.txt", "a") as file: #This is going to open a file and the be able to W or white to the file changed it to a for appending, also put with so you won't need a close function
    file.write(f"{name}\n")
"""
"""
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) #this will remove the /n that is involved with files and prints

for name in sorted(names):
    print(f"hello, {name}")
"""

