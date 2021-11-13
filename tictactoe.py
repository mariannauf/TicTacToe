"""
Step 1: board
Step 2: display board
Step 3: play game
Step 4: handle turn
Step 5: check win (if game over)
    5.1: check rows
    5.2: check columns
    5.3: check diagonals
Step 6: check tie
Step 7: flip player
"""

#----Global Variables-----

#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#if is still going
game_still_going = True

#Who won?
winner = None

#Who's turn is it
current_player = "X"

#display board
def display_board():
    print(board[0] + "|" +board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

#Play a game of tic tac toe
def play_game():
    #Display the initial board
    display_board()

    #while the game is still going
    while game_still_going:
        
        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the game has player
        flip_player()


#The game has ended
if winner == "X" or winner =="O":
    print(winner + " won")
elif winner == None:
    print("It's a tie.")
    
#Handle a single turn of an arbitrary player    
def handle_turn(player):
    position_str = input("Choose a position from 1 to 9: ")
    position = int(position_str) - 1 #since board has positions 0-8 we need to subtrace one from position so it knows excatly where to go

    board[position] = "X"

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #set up global variables so that winner is inside the scope of check_for_winner
    global winner
    
    #check row
    row_winner = check_row()
    #check columns
    columns_winnr = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:

        winner = row_winner()
        
    elif column_winner:
        
        winner = column_winner()
        
    elif diagonal_winner:
        
        winner = diagonal_winner()
        
    else:
        
        winner = None
        
    return

#check rows
def check_rows():
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    return

#check colums
def check_columns():
    column_1 = board[1] == b
    return

#check diagonals
def check_diagonals():
    return

def check_if_tie():
    
    return

def flip_player():
    return


play_game()
