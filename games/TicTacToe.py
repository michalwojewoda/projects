import random


# starting with creation of a board

def display_board(board):
    print('\n' * 100)
    print("    |     |   ")
    print(" " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("----|-----|----")
    print(" " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("----|-----|----")
    print(" " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("    |     |   ")


board = ["#", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
print(display_board(board))
print(display_board(board))


# assign players

def player_input():
    '''
    Output is tuple = (player 1 marker, Player 2 marker)
    '''
    marker = ""
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()

    if marker == "x":

        return ("X", "O")
    else:
        return ("O", "X")


# Write function that takes in the board list object, a marker,
# and desired position number 1-9 and assign it to the board.

def place_marker(board, marker, position):
    board[position] = marker


# write a function that takes in a board and mark x o and then checks to see if that mark has won

def win_check(board, mark):
    # return boolean to check if true or false

    return ((board[7] == board[8] == board[9] == mark) or  # across
            (board[4] == board[5] == board[6] == mark) or  # across
            (board[1] == board[2] == board[3] == mark) or  # across
            (board[7] == board[4] == board[1] == mark) or  # down
            (board[8] == board[5] == board[2] == mark) or  # down
            (board[9] == board[6] == board[3] == mark) or  # down
            (board[7] == board[5] == board[3] == mark) or  # diagonal
            (board[9] == board[5] == board[1] == mark))  # Diagonal


# Random module - to randomly choose player that goes first

def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


# booleaon that indicate free space on the board

def space_check(board, position):
    return board[position] == " "


# check if the board is full #Day2

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True  # that says boar is full


# players next position

def playerchoice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('choose a position (1-9) '))
    return position


# ask player if he want to play again

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# Logic

# first while looop to keep running the game

print("Do you want to play Tic Tac Toe")

while True:
    # play the game

    ## set evertytnig up

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Ready to play? y or n: ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

        ##Game play

    while game_on:

        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = playerchoice(the_board)

            # place the marker on the position
            place_marker(the_board, player1_marker, position)

            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    break
                # no tie and no win? then next players turn
                else:
                    turn = "Player 2"



        ##Player 1

        else:

            display_board(the_board)
            # choose a position
            position = playerchoice(the_board)

            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('player 2 has won!')
                game_on = False
            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    break
                # no tie and no win? then next players turn
                else:
                    turn = "Player 1"

    if not replay():
        break

# Break out of the while loop on replay