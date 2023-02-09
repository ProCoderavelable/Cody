print ("This code calcuates how many times you must roll a six-sided dice before you get a 6 ")

import random

def roll_dice():
    return random.randint(1, 6)

def calculate_average_rolls_to_get_6():
    overall_rolls = 0
    total_attempts = 0
    total_sum = 0
    total_avg = 0
    while True:
        roll = roll_dice()
        overall_rolls += 1
        total_attempts += 1
        if roll == 6:
            average_rolls = overall_rolls / total_attempts
            total_sum = total_sum + average_rolls
            overall_rolls = 0
        if total_attempts == 100:
            break
    total_avg = total_sum / total_attempts

calculate_average_rolls_to_get_6()