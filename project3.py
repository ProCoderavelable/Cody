print ("if you dont go to the bathroom before you eat you will be sick  you dont go to lunch you will be hungry if you dont make it to class on time you will be marked tardy by Mr. Jones")
########
#import modules
import os
#######

########
#define functions
#######
def start():
    print("Welcome!")
    b130()
def check_time():
    os.system('clear')
    global minutes
    minutes = minutes + 1
    if minutes >= 5:
        tardy()
def tardy(): 
    print ("you are late and marked tardy by Mr. Jones")
    exit()

def b130():
    check_time()
    print("You are in b130")
    if hungry==True:
        print("you are still hungry so you need to go to the cafeteria ")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbathroom\n\twaterfountain\n\tcafeteria\n")
    if move.lower() == "bathroom":
        bathroom()
    elif move.lower() == "waterfountain":
        waterfountain()
    elif move.lower() == "cafeteria":
        cafeteria()
    else: 
        print("that was not one of the options") 
        b130()

        #TODO: what should happen if they type something else? 

def waterfountain():
    check_time()
    print("You are in waterfountain")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbathroom\n\tcafeteria\n\tb130\n")
    if move.lower() == "bathroom":
        bathroom()
    elif move.lower() == "b130":
        b130()
    elif move.lower() == "cafeteria":
        cafeteria()
    else: 
        print("that was not one of the options")
        waterfountain()
        #TODO: what should happen if they type something else?

def cafeteria(): 
    check_time()
    print("You are in cafeteria")
    global hungry
    hungry=False
    if handsarewashed==False: 
        print("you are sick because you didn't wash your hand in the bathroom.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbathroom\n\twaterfountain\n\tb130\n")
    if move.lower() == "bathroom":
        bathroom()
    elif move.lower() == "waterfountain":
        waterfountainoom3()
    elif move.lower() == "b130":
        b130()
    else: 
        print("that was not one of the options")
        cafeteria()
        #TODO: what should happen if they type something else?

def bathroom(): 
    check_time()
    print("You are in bathroom and you washed your hands") 
    global handsarewashed
    handsarewashed=True
    move = input("\nWhere would you like to go? Say one of these choices:\n\tb130\n\twaterfountain\n\tcafeteria\n")
    if move.lower() == "b130":
        b130()
    elif move.lower() == "waterfountain":
        waterfountain()
    elif move.lower() == "cafeteria":
        cafeteria()
    else: 
        print("that was not one of the options")
        bathroom()
        #TODO: what should happen if they type something else?


########
#main
#######
#TODO: Add some global variables
handsarewashed=False

minutes = 0

hungry=True

start()