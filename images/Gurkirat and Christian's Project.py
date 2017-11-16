import random   # Imports a random integer
import sys   # Creates a system


def guess_game():   # defines the game
    n = random.randint(1, 99) # n is equal to an integer between 1 and 99
    start(n)   #starts game intiative
def start(n): # defines the start of the game
  
    guess = raw_input("Enter an integer from 1 to 99: ")# guess equals the raw input
    
    if guess == "end":# if "end" is entered the game is over
        sys.exit() #syetem end
    
    
    try:# the program tries this operation
     guess = int(guess) # indicates the integer guess
    except ValueError: # it eradicates the Error
     print("That's not an int!") #states that the input is not an integer
     guess = int(raw_input("Enter an integer from 1 to 99: ")) # sends program back to the start
    while 0 == 0: # Always repeats
        a = int(guess)  # a equals to the guess      
        if a < n:  # if a is less than n
            print "guess is low"    # indicates that guess is low
            start(n) # Restarts program
        elif a > n:#if a is greater than n
            print "guess is high" # indicates that the guess is too high
            start(n) # Restarts program
        elif n == a: # if a equals n
                    print "you guessed it!" # indicate that you won
                    sys.exit()  #Ends program

    
