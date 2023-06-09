# using it for matrix purpose
import numpy as np
#using it for GUI
import pygame
#using is for exiting the system window that py game shows
import sys
import math

#RGB values
BLUE = (50,116,255)
BLACK = (25,25,25)
RED = (222, 19, 19 )
YELLOW = (209, 222, 19)


ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    # 6 rows and 7 columns
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#chnage the orentation of the borad (0,0) come at bottomost left
def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    #check horizontal loc for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
           if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
               return True

    # Check for vertical loc for win
    for c in range(COLUMN_COUNT ):
        for r in range(ROW_COUNT - 3):
           if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
               return True

    #Check for postively sloped diagnols
    for c in range(COLUMN_COUNT -3 ):
        for r in range(ROW_COUNT - 3):
           if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
               return True


    # Check for negatively sloped diagnols
    for c in range(COLUMN_COUNT -3 ):
        for r in range(3, ROW_COUNT):
           if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
               return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] ==1:
                   pygame.draw.circle(screen, RED,(int(c * SQUARESIZE + SQUARESIZE / 2), height- int(r * SQUARESIZE + SQUARESIZE / 2)),RADIUS)
            elif board[r][c] ==2:
                   pygame.draw.circle(screen, YELLOW,(int(c * SQUARESIZE + SQUARESIZE / 2), height- int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    pygame.display.update()
 # Initislaing board varaiable
board = create_board()
game_over = False
turn = 0

pygame.init()
#one box size in pixel
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

RADIUS = int(SQUARESIZE/2 - 5)

size = (width, height)
#to display that screen
screen = pygame.display.set_mode(size)
#To draw the board
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("Tahoma",75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)

             # Ask for player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("PLAYER 1 WINS!!", 1,RED)
                        screen.blit(label,(75,10))
                        game_over = True

            # Ask for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("PLAYER 2 WINS!!", 1, YELLOW)
                        screen.blit(label, (75, 10))
                        game_over = True


            print_board(board)
            draw_board(board)

            # Using it for alternating the p1 and p2 chnace
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(4000)

