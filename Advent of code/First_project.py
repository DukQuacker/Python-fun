#Advent of code problem 1 done by Zach Breazile

#Asks for a user input then runs calibration_values with said value
def main():
    user_string = input("Please input a string: ")
    calibration_value(user_string)

#This will find the first and last number in a given string
def calibration_value(string):
    #starter values for function to run
    element_one = 0
    element_two = 0
    position = 0
    first_position = 0
    for elements in string: 
        position += 1
        if elements.isdigit() and first_position == 0: #finds a int value and sets it to the first element_one exp: h3l3 would be element_one = 3
            element_one = elements
            first_position = position
        elif first_position < position and elements.isdigit(): #finds the second element and sets it to element_two exp: h3l2 would be element_two=2
            element_two = elements
    if element_two == 0: #If nothing was definded or could be found as a second element it will set the first element to the second element
        element_two = element_one

    print(element_one + element_two) #combines the numbers exp 3 + 2 = 32

main() #runs program
