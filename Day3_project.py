#simple project to use imput if statements, user_inputs and imports
#You will need the Pillow library to be able to run this program.

from PIL import Image

print("Welcome adventurer to the world of university")
print("It looks like you have a paper due in 2 days and you still have yet to work on it.")
print("1. Do your work")
print("2. Do it tomorrow")
print("3. Let ChatGPT do it")
print("4. Drop out")
user_input = int(input("What will you choose? "))
if user_input == 1:
    print("You slay the paper with your skills in wrighting that you never thought was possible")
elif user_input == 2:
    print("You take a nap and its soon tomorrow")
    print("You headover to your computer and you see only one word")
    im = Image.open("essay_image.JPG")
    im.show()
elif user_input == 3:
    print("You let the AI do the paper and your you've been found out using the tool and kicked out of school")
elif user_input == 4:
    print("You leave your room with all your belongings and go live your best life free of the paper")
else:
    print("You put in the wrong input that you never thought of and the paper explodes in front of you")



