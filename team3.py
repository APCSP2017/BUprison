####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

from __future__ import print_function
import matplotlib.pyplot as plt # standard short name
import random


team_name = 'Rushed' # Only 10 chars displayed.
strategy_name = 'Always Opposite'
strategy_description = 'Do the opposite of oppents last choice'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    x=len(my_history)
    them=len(their_history)-1    
    
    if x==0:
        pick=random.choice(['c','b'])
        return pick
    else:
        if their_history[them]=='c':
            return 'b'
        else:
            return 'c'
            
    
        
    
    
    
    
    
    
    
    
    
    
    
    return 'c'














    
