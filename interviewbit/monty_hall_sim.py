#choice between 3 doors, goat, goat, and a car....

import random 
#first generate the user choosing the door
choice = input("Which door contains the brand NEW car?")

car = random.randint(1, 3)
if choice == car:
    print("You've just won a brand new CAR!!!")
else:
    print("Oh, I'm sorry, but you have two more doors to choose from, which one is it: ") 
