"""
Step 1: board
Step 2: display board
Step 3: play game
Step 4: handle turn
Step 5: check win
    5.1: check rows
    5.2: check columns
    5.3: check diagonals
Step 6: check tie
Step 7: flip player
"""

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
    print(board[0] + "|" +board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

    display_board()
