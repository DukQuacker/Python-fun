profits = []
exit_loop = "0"
sum = 0

def isfloat(point):
    try:
        float(point)
        res= True
    except:
        res= False
    return res

print("Hello user you will be inputing how many numbers you like until you're finished")
while exit_loop == "0":
    profit = input("Please input your numbers: ")
    num_float = isfloat(profit)
    if profit.isnumeric() == True or num_float == True:
        profits.append(profit)
    else:
        print("Please input a working number")
    exit_loop = input("Would you like you exit the loop [0 == NO] or [1 == YES]: ")

for x in profits:
    sum += float(x)

print(f'Your total is ${sum:.2f}')
print(f'Your average is ${sum//len(profits)}')

