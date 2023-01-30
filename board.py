from square import Square
import pygame

class Board:

    __board_size: int = (8,8)
    __square_list = []
    ship_list = [[''], ['',''], ['','',''], ['','', '',''], ['','','','','']]

    def __init__(self, type, screen):
        self.__type = type      #define where to place the board. Player(0) left side of screen, Computer(1) right side of screen. 
        self.__screen = screen
        self.draw_board()       #draw the board to the screen

    def check_if_square_clicked(self):
        mpos = pygame.mouse.get_pos() # Get mouse position

        for i in range(0, 64):
            square_x, square_y, letter = self.__square_list[i].getLocation()[0][0], self.__square_list[i].getLocation()[0][1], self.__square_list[i].getLocation()[1]
            if mpos[0] >=  square_x and mpos[0] <= square_x + 25:
                if mpos[1] >= square_y and mpos[1] <= square_y + 25:
                    return letter

        return False
        
    def set_square_colour(self, arr):
        __size = (25,25)


        for letter in arr:
            for i in range(0, 64):
                if self.__square_list[i].getLocation()[1] == letter:
                    x = self.__square_list[i].getLocation()[0][0]
                    y = self.__square_list[i].getLocation()[0][1]
                    if self.__type:
                        x += 300
                    self.__square_list[i].setEmpty(False)
                    pygame.draw.rect(self.__screen, pygame.Color((255,0,0)), (x, y, __size[0], __size[1]))
                    pygame.draw.rect(self.__screen, pygame.Color((0,0,0)), (x, y, __size[0], __size[1]), width=1)
                    font = pygame.font.Font('freesansbold.ttf', 10)
                    text = font.render(letter, True, (0,0,0))
                    self.__screen.blit(text, (x + 5, y + 5))
                    pygame.display.flip()



    def draw_board(self):
        __x = 0
        __y = 0
        __size = (25,25)
        __border_thickness = 1

        __letter_code = 97

        if self.__type:
            __x = 300

        for i in range(0, self.__board_size[0]):
            for j in range(0, self.__board_size[1]):
                __x += 25
                self.__square_list.append(Square(__x, __y, str(chr(__letter_code)) + str(j+1)))

                pygame.draw.rect(self.__screen, pygame.Color((255,255,255)), (__x, __y, __size[0], __size[1]))
                pygame.draw.rect(self.__screen, pygame.Color((0,0,0)), (__x, __y, __size[0], __size[1]), width=__border_thickness)

                font = pygame.font.Font('freesansbold.ttf', 10)
                text = font.render(str(chr(__letter_code)) + str(j+1), True, (0,0,0))
                self.__screen.blit(text, (__x + 5, __y + 5))

                pygame.display.flip()

            __letter_code += 1

            if self.__type:
                __x = 300
            else:
                __x = 0
            __y += 26


