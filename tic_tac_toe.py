import random
print("Welcome to Tic Tac Toe")
def display_board(board):
    print()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4] +'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1] +'|'+board[2]+'|'+board[3])
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
def player_input():
    marker=""
    while marker!='X' and marker!='O':
        marker=input("Player 1, Select your marker: ")
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)

def place_marker(board,marker,position):
    board[position]=marker



def win_check(board,mark):


    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
        (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
        (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
def toss():
    if random.randint(0,1)==0:
           return 'Player 2'
    else:
            return 'Player 1'
def space_check(board,position):
    return board[position]==' '
def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in list(range(1,10)) or not space_check(board,position):
        position=int(input('Whats your next position:'))
    return position
def replay():
     return input("DO you want to play again: ").lower().startswith('y')


while True:
    Board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=toss()
    print(turn+' will go first.')
    lets_play=input('Are you ready to play? ')
    if lets_play.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    b=replay();

    while game_on and b:
        if turn=='Player 1':
            display_board(Board)
            print('Player 1 '+player1_marker)
            position=player_choice(Board)
            place_marker(Board,player1_marker,position)
            if win_check(Board, player1_marker):
                display_board(Board)
                print('Congrats player 1 won!+++++')
                game_on=False
            else:
                if full_board(Board):
                    display_board(Board)
                    print('The game is draw!')
                    break
                else:
                    turn='Player 2'
        else:
            display_board(Board)
            print('Player 2 '+player2_marker)
            position = player_choice(Board)
            place_marker(Board, player2_marker, position)

            if win_check(Board, player2_marker):
                display_board(Board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'


    if not replay():
        break










