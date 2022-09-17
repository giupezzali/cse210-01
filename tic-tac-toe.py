#CSE 210 - W01 Prove: Developer "Tic-Tac-Toe"  
#Author: Giuliana Pezzali

"""
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, 
a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

Rules
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.
"""


from colorama import Fore, Back, Style


grid = [1,2,3,4,5,6,7,8,9] 
def main():
    
    print('\nWelcome to Tic-Tac-Toe game!\n')
    display_grid()
    
    while True:
        if possible_victories(grid):
            print('Good game. Thanks for playing!')
            break
        elif is_full(grid):
            print('Good game. Thanks for playing!')
            break
        else:
            player1 = int(input("\nx's turn to choose a square (1-9): "))
            print()
            replace_grid(player1, (Fore.MAGENTA + 'x'))
            display_grid()
            if possible_victories(grid):
                print('Good game. Thanks for playing!')
                break
            elif is_full(grid):
                print('Good game. Thanks for playing!')
                break
            else:
                player2 = int(input("\no's turn to choose a square (1-9): \n"))
                print()
                replace_grid(player2, (Fore.CYAN + 'o'))
                display_grid()
                possible_victories(grid)
                is_full(grid)


def display_grid():
    #This function displays a grid with the available spaces to play.
    print(f'{grid[0]}|{grid[1]}|{grid[2]} \n-+-+- \n{grid[3]}|{grid[4]}|{grid[5]} \n-+-+- \n{grid[6]}|{grid[7]}|{grid[8]}')

def replace_grid(player, sign):
    #replace_grid will replay the available spaces with x's and 0's
    for i in grid:
        if player == i:
            player -= 1
            grid[player] = sign


def possible_victories(grid):
    #evaluate possible victories and return if applicable 
    return grid[0] == grid[1] == grid[2] or grid[3] == grid[4] == grid[5] or grid[6] == grid[7] == grid[8] or grid[0] == grid[3] == grid[6] or grid[1] == grid[4] == grid[7] or grid[2] == grid[5] == grid[8] or grid[0] == grid[4] == grid[8] or grid[2] == grid[4] == grid[6]

def is_full(grid):
    #verify if the grid is full
    return (grid[0] == 'x' or grid[0] == 'o') and (grid[1] == 'x' or grid[1] == 'o') and (grid[2] == 'x' or grid[2] == 'o') and (grid[3] == 'x' or grid[3] == 'o') and (grid[4] == 'x' or grid[4] == 'o') and (grid[5] == 'x' or grid[5] == 'o') and (grid[6] == 'x' or grid[6] == 'o') and (grid[7] == 'x' or grid[7] == 'o') and (grid[8] == 'x' or grid[8] == 'o')


if __name__ == "__main__":
    main()