'''
Solo Checkpoint 02
Author: Bro. Hayes
'''

from tkinter.messagebox import RETRY


def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    player = next_player("")
    board = create_board()
    while not is_winner and not is_draw:
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    if is_winner == "x":
        print("Congrats player x!")
    elif is_winner == "y":
        print("Congrats player o!")
    else:
        print("Thanks for playing!")


def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for square in range(9):
        board.append(square + 1)
        return board


def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("=-=")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("=-=")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    for square in range[9]:
        if board[square] != "x" and board[square] != "o":
            return False
    return True


def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    return (board[0]==board[1]==board[2]or
            board[3]==board[4]==board[5]or
            board[6]==board[7]==board[8]or
            board[0]==board[4]==board[8]or
            board[0]==board[3]==board[6]or
            board[1]==board[4]==board[7]or
            board[2]==board[5]==board[8]or
            board[2]==board[4]==board[6])
            

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    chosen = int(input(f"{player}'s choice (0-8)"))
    board[chosen - 1] = player    


def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == "" or current=="0":
        return "x"


if __name__ == "__main__":
    main()
