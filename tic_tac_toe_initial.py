import os
import re

def print_board(board):
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            if 0 < move:
                if board[i*3+j] == 1:
                    print('X', end="")
                elif board[i*3+j] == 0:
                    print('O', end="")
                else: 
                    print(' ', end="")
            elif board[i*3+j] != -1:
                print(board[i*3+j], end="") #print board with instruction numbers
            else:
                print(' ', end="")
            
            if j != 2:
                print(" | ", end="")
        
        if i != 2:
            print("\n""-----------")
    print("\n")

def print_instruction():
	print("You can use the folling numbers to make your move\n")
    #print("The board look like this: )
	print_board([1,2,3,4,5,6,7,8,9])

def user_input(player):
    valid = False
    while not valid: 
        try: 
            print()
            user = input("Turn - Player " + player + " - Where would you " +
                        "like to place the " + player + " mark? ")
            print('\n')
            user = int(user)
            if user >=1 and user <= 9: 
                return user - 1
            else: 
                print("That is not a valid move, please try again.\n")
        except Exception as e:
            print("This is not a valid move, please try again.\n")

#main
clear = os.system('cls' if os.name == 'nt' else 'clear')
move = 0
player = 'X'
board = [' '] * 9
win = False

print_instruction()

while not win:
    move += 1
    user = user_input(player)
    
    if move % 2 == 0:
        player = 'X'
    else: 
        player = 'O'
    
    if player == 'O':
        board[user] = 1
    else:
        board[user] = 0
    print_board(board)