#!/usr/bin/python3
"""jamesAlbert | hjalbert@amazon.com

Lab 48: MINI PROJECT #1: IF-LOGIC SCRIPT

This project will randomly generate a number at runtime 

The user will then have to guess the number until they guess correctly """

def main():
    """This is runtime code block"""
    print("start")
    #import required modules
    import random

    # first things first we need to "randomly" generate a number 
    rand_int = random.randint(0,100)
    
    #declare global user_input so we can access this variable inside the while loop
    global user_input
    user_input = int(input("guess a number between 1 and 100"))
    
    #give some response to user
    print("you guessed", user_input)
    
    #verify that the number is in a valid range
    if user_input > 1 or user_input < 100:
        #in the lucky chance the user guesses it correct on the first try 
        if user_input == rand_int:
            print("lucky guess!")
        
        #actual loop where the user will play the game
        while rand_int != user_input:
            #find the relative distance the user is away from the answer
            difference = rand_int - user_input
            
            #play game of hot and cold
            if abs(difference) > 75: print("way off")
            elif abs(difference) > 50 and abs(difference) <= 75: print("off")
            elif abs(difference) > 25 and abs(difference) <= 50: print("getting  closer")
            elif abs(difference) > 12 and abs(difference) <= 25: print("close")
            elif abs(difference) > 0 and abs(difference) <= 12: print("very close")
    
            user_input = int(input("guess again"))

        #win case!
        print("correct")

if __name__ == "__main__":
    main()
