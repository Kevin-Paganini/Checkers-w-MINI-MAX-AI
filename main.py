
import pygame
from checkers.constants import WIDTH, HEIGHT, WHITE
from checkers.board import Board
from checkers.constants import SQUARE_SIZE, RED
from checkers.game import Game
from minimax.algorithm import minimax


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


pygame.display.set_caption("Checkers 3000")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    game = Game(WIN)
    clock = pygame.time.Clock()
    
    win = ''
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 10, WHITE, game)
            game.ai_move(new_board)


        if game.winner() != None:
            if game.winner() == (255, 0, 0):
                win = 'RED IS THE WINNER'
                run = False
            else:
                
                win = 'WHITE IS THE WINNER'
            print(win)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col  = get_row_col_from_mouse(pos)
                
                    
                game.select(row, col)
                
        
        game.update()

    pygame.quit()

main()