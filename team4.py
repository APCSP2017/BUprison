####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
#####

team_name = 'Barnyard Gals' # Only 10 chars displayed.
strategy_name = 'Be nice until you f us'
strategy_description = 'Use the teams history to determine our play'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''
    if len(my_history)==0: 
        return 'c'
    else:
        if their_history.count('b')> 2*their_history.count('c'):
            return 'c'
        elif 0.5*their_history.count('c') < their_history.count('b') and their_history.count('b') <= 2*their_history.count('c'):
            for a in range(len(my_history)):
                if my_history[a] == 'c':
                    return 'b'
                else:
                    return 'c'
        else:
            return 'b'
   