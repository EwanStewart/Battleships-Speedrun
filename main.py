import pygame, sys
from board import Board


def create_window():    
    size = (600, 600)
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color((255,255,255)))
    pygame.display.flip()
    return screen

def create_board(screen):
    player = Board(0, screen)
    computer = Board(1, screen)
    return player, computer




def main():
    pygame.init()
    screen = create_window()
    player_board, computer_board = create_board(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                result = player_board.check_if_square_clicked()
                if (result):
                    print(result)


            if event.type == pygame.QUIT: sys.exit()


if __name__ == "__main__":
    main()