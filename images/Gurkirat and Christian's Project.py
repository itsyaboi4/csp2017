import random
import sys


def guess_game():
    n = random.randint(1, 99)
    start(n)
def start(n):
  
    guess = raw_input("Enter an integer from 1 to 99: ")
    
    if guess == "end":
        sys.exit()
    
    
    try:
     guess = int(guess)
    except ValueError:
     print("That's not an int!")
     guess = int(raw_input("Enter an integer from 1 to 99: "))
    while 0 == 0:
        a = int(guess)        
        if a < n:
            print "guess is low"
            start(n)
        elif a > n:
            print "guess is high"
            start(n)
        elif n == a:
                    print "you guessed it!"
                    sys.exit()

    
