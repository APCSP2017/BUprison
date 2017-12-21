####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'GoChem' # Only 10 chars displayed.
strategy_name = 'Check my history and  their history  to mine '
strategy_description = 'Check even give b or random b or c' 
    

import random
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history)%2:
        return 'b'
        if len(their_history)%3:
            return random.choice(['b','c'])
#Make my move based on the history with this player.
    
 #   if their length is even return b and if their length %3 then the random will 
  #  pick c or b.
    
   # Returns 'c' or 'b' for collude or betray.