# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math


# initialize global variables used in your code
secret_number = 0
num_range = 100
allowed_guess = 0
count = 0


# helper function to start and restart the game
def new_game():
    global secret_number, num_range, allowed_guess, count
    count = 0
    base = 2
    allowed_guess = math.ceil(math.log(num_range - 0 + 1, base))
    print "New game: Range is from 0 to %d" %num_range
    print "Number of remaining guess is %d\n" %allowed_guess
    secret_number = random.randrange(0, num_range)


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, allowed_guess
    num_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, allowed_guess
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, allowed_guess, count
    print "Guess was %s" %guess
# Increment the guess count by 1 for every input
    count = count + 1
# Validation if exceeded the number of guesses    
    if count < allowed_guess:   
        # Validate the guess
        if int(guess) < secret_number:
            print "Number of remaining guesses is %d" %(allowed_guess-count)
            print "Higher!\n"
        elif int(guess) > secret_number:
            print "Number of remaining guesses is %d" %(allowed_guess-count)
            print "Lower!\n"
        else:
            print "Number of remaining guesses is %d" %(allowed_guess-count)
            print "Correct!\n"
            new_game()    
    elif count == allowed_guess:
        print "Number of remaining guesses is %d" %(allowed_guess-count)
        # If in the last guess, player's guess is correct, he/she wins
        if int(guess) == secret_number:
            print "Correct!\n"
        else:
            print "Game over: You ran out of guesses. The number was %d\n" %secret_number
        new_game()
        

    # create frame
frame = simplegui.create_frame('Guess the number', 200, 200)



# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_input('Ener a guess', input_guess, 100)

# call new_game and start frame
new_game()
frame.start()
