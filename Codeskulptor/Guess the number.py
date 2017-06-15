# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui, random

num_range = 100
player_num =0
player_guess_times = 0

# helper function to start and restart the game
def new_game():
    global num_range, player_num, player_guess_times
    
    if (num_range==100):
        player_guess_times = 7
    else:
        player_guess_times = 10
        
    player_num = random.randrange(0,num_range)
    print ''
    print 'New game, Range is from 0 to ', num_range
    print 'You have ', player_guess_times, ' chances to guess.'
    # remove this when you add your code    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    #print num_range
    num_range = 100
    # remove this when you add your code    
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range =1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global player_guess_times
    
    guess_num = int(guess) 
    
    player_guess_times -= 1
    
    print ''
    print 'You guessed: ', guess_num, '. ' 
    print 'You have ', player_guess_times, ' chances to guess.'
    
    if (int(guess) == player_num):
        print 'You are correct!'
        new_game()
    elif (int(guess) < player_num):
        print 'Higher!'
    else:
        print 'Lower!'
    


# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame

frame.add_button('Range is [0,100)', range100, 200)
frame.add_button('Range is [0,1000)', range1000, 200)
frame.add_input('Enter a guess', input_guess, 200)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
