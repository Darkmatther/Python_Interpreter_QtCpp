# Author: abekohen
# https://gist.github.com/abekohen/9955561

# Rock-paper-scissors-lizard-Spock
# COURSERA Python simple project

# equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# random.randrange() so we need to import random
import random

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

    
# test code 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
