# Author: abekohen  (slightly adapted by Matthieu Kieffer to be ran with command line arguments)
# https://gist.github.com/abekohen/9955561

"""
    Description:
    A simple rock/paper/scissors/lizard/spock game. 
	Enter your choice as a command line argument. Example: python RockPaperScissorsLizardSpock.py scissors
"""

import sys
import random

items = ["rock", "paper", "scissors", "lizard", "spock"]

def name_to_number(name):
    
    if (name == "rock"): return 0
    if (name == "Spock"): return 1
    if (name == "paper"): return 2
    if (name == "lizard"): return 3
    if (name == "scissors"): return 4
    return -1
   

def number_to_name(number):
    
    if (number == 0): return "rock"
    if (number == 1): return "Spock"
    if (number == 2): return "paper"
    if (number == 3): return "lizard"
    if (number == 4): return "scissors"
    return "Bad number entered"

	
def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print 

    # print out the message for the player's choice
    print "Player chooses", player_choice 

    # convert the player's choice to player_number 
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    
    # convert comp_number to comp_choice
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice 
    
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5

    # determine winner, print winner message
    if (diff == 1 or diff == 2): winner = "Computer"
    elif (diff == 3 or diff == 4): winner = "Player"
    elif (diff == 0): winner = "Tie"    
    else: winner = ""
        
    if (winner == "Tie"): print "Player and computer tie!"
    else: print winner, "wins!"    


if __name__ == "__main__":

    choices = "\
Possible choices are:\n\
- rock\n\
- paper\n\
- scissors\n\
- lizard\n\
- spock\n\
Example: rock lizard paper paper\n"

    #Check if the user has entered at least one command line argument
    if(len(sys.argv) < 2):
        print "\nERROR: The game couldn't be started.\nPlease enter your choice (or a sequence of choices) as a command line argument, and then re-run the program.\n", choices

    #Play the game for each command line input from the user
    for i, arg in enumerate(sys.argv[1:]):
        if arg in items:
            rpsls(arg)
        else:
            print "\nERROR: there is a mistake in the input argument number", str(i), ":", arg,"\n", choices
            break


