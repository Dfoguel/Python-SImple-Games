import random

def play():
    user = input("What\'s your choice? 'S' for scisors, 'P' for paper, 'R' for rock\n").lower()
    computer = random.choice(['r','p','r'])
    print(f"computer plays {computer}... ")

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost...'

def is_win(player, opponent):
    #return True if player wins
    if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's'):
        return True
    
print(play())
