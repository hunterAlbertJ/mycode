

try:
    user_input = int(input("how many bottles of beer? Must be between 1 and 100 "))
    
    for x in range(user_input):
        print(user_input - x, "bottles of beer on the wall!")
        print(user_input -x, "bottles of beer on the wall!", user_input -x,"bottles of beer! You take one down, pass it around!")
        
except ValueError:
    print("Oops!  That was no valid number.  Try again...")


