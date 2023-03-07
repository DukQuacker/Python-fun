#while loop

""" name =""

while len(name) == 0:
    name = input("please enter your name: ")

print("hello " + name) """

#for loop

""" for i in range(10):
    print(i+1)

for i in range(50,100+1,2): #can take 3 arguments starting, where its going, and step
    print(i)

for i in "Bro code":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year!") """

#nested loops

""" rows = input("How many rows?: ")
columns = input("How many columns?: ")
symbol = input("Ender a symbol to use: ")

for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end="")
    print() """

#lists

""" food = ["apple", "banana", "cherry", "pizza", "pudding"]

food[0] = "sushi"

food.append("ice cream") 
food.remove("banana") 
food.pop()
food.insert(0,"cakes")
food.sort()
food.clear()

for x in food:
    print(x) """

#2d lists
""" 
drinks = ["coffee" , "soda" , "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks,dinner,dessert]

print(food[2][1])
 """
#tuples = collection which is ordered and unchangeable used to group together related data

""" student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))

for x in student:
    print(x)

if "bro" in student:
    print("bro is here")
 """

#Set = collection which is unordered, unindexed, No duplicate values

""" utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate","cup","knife"}


#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)


for x in utensils:
    print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes)) """

#dictionary = A changeable, unordered collection of unique key:value
#pairs. Fast because they is hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC",
            "India": "New Dehli",
            "China":"Beijin",
            "Russia":"Moscow"}

#print(capitals["Germany"])
#print(capitals.get("germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las vegas"})
capitals.pop("China")

for key,value in capitals.items():
    print(key,value)