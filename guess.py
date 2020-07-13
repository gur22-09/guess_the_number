# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math



# helper function to start and restart the game
guess_range = 100
secret_number = random.randrange(0,100)
guess_left = math.ceil(math.log(guess_range + 1)/math.log(2))
def new_game():
    # initialize global variables used in your code here
    global guess_left
    
    guess_left = math.ceil(math.log(guess_range + 1)/math.log(2))
    print 'New Game Range is from 0 to '+str(guess_range)
    print 'Number of guess left '+str(guess_left)+'\n'


# define event handlers for control panel
def range100():
    global secret_number,guess_range
    # button that changes the range to [0,100) and starts a new game 
    secret_number = random.randrange(0,100)
    guess_range = 100
    #calling new game function to restart game
    new_game()
   

def range1000():
    global secret_number,guess_range
    # button that changes the range to [0,1000) and starts a new game     
    secret_number = random.randrange(0,1000)
    guess_range = 1000
    #calling new game function to restart game
    new_game()
    
def input_guess(guess):
    global guess_left
    # main game logic goes here	
    input = int(guess)
    
    
    print 'Guess was '+guess
    if(guess_left == 1):
        print 'You ran out of guesses. The correct Number was '+str(secret_number)+'\n' 
        new_game()
        
    elif (input > secret_number):
        guess_left -= 1
        print 'Number of guess left '+str(guess_left)
        print 'Lower!\n'
    elif(input < secret_number):
        guess_left -= 1
        print 'Number of guess left '+str(guess_left)
        print 'Higher!\n'
    else:
        print 'Correct!\n'
        new_game()
        
        
    

    
# create frame
frame = simplegui.create_frame('Guess the Number',100,200)
frame.add_input('Enter Guess',input_guess,100)
frame.add_button('Range is [0,100)',range100)
frame.add_button('Range is [0,1000)',range1000)


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
