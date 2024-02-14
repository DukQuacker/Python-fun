#learning about Exceptions
'''
try:
    x = int(input("what's x? ")) #want to put try in functiosn that could throw an error50
except ValueError:
    print("x is not an interger") #if error of Valueerror comes up exacute this code
else:
    print(f"x is {x}") #If nothing else print x 
'''
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: #infinite loop
        try:
            return int(input("what's x? ")) #want to put try in functiosn that could throw an error50
        except ValueError:
            print("x is not an interger") #if error of Valueerror comes up exacute this code

main()
'''
#example of pass
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: #infinite loop
        try:
            return int(input("what's x? ")) #want to put try in functiosn that could throw an error50
        except ValueError:
            pass
        
main()