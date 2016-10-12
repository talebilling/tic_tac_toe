import os
import re

def print_board(board):
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            #print X or O, after user gave input
            if 0 < move_count:
                if board[i*3+j] == 1:
                    print('X', end="")
                elif board[i*3+j] == 0:
                    print('O', end="")
                else: 
                    print(' ', end="")
            #print board with instruction numbers
            elif board[i*3+j] != 'filled in':
                print(board[i*3+j], end="") 
            else:
                print(' ', end="")
            #print sepatation wall
            if j != 2:
                print(" | ", end="")
        #print sepatation wall
        if i != 2:
            print("\n""-----------")
    print("\n")

def print_instruction():
	print("You can use the folling numbers to make your move:\n")
	print_board([1,2,3,4,5,6,7,8,9])

def user_input(player):
    while True: 
        try: 
            player_input = input("Turn: Player " + player + " - Where would you " +
                        "like to place the " + player + " mark? ")
            print('\n')
            player_input = int(player_input)
            if player_input >=1 and player_input <= 9: 
                return player_input - 1
            else: 
                print("That is not a valid move, please try again.\n")
        except Exception as e:
            print("This is not a valid move, please try again.\n")

def check_win():
    print

def quit_game():
    print

#main
clear = os.system('cls' if os.name == 'nt' else 'clear')
board = [' '] * 9
move_count = 0
player = 'X'
win = False

print_instruction()

while not win:
    move_count += 1
    player_input = user_input(player)
    
    if move_count % 2 == 0:
        player = 'X'
    else: 
        player = 'O'
    
    if player == 'O':
        board[player_input] = 1
    else:
        board[player_input] = 0
    print_board(board)


check_win()
quit_game()