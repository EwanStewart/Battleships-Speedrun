from square import Square
import pygame
import random

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
        
    def set_square_colour(self, arr, c):
        __size = (25,25)
        for letter in arr:
            for i in range(0, 64):
                if self.__square_list[i].getLocation()[1] == letter:
                    x = self.__square_list[i].getLocation()[0][0]
                    y = self.__square_list[i].getLocation()[0][1]
                    if self.__type:
                        x += 300
                    self.__square_list[i].setEmpty(False)
                    pygame.draw.rect(self.__screen, pygame.Color(c), (x, y, __size[0], __size[1]))
                    pygame.draw.rect(self.__screen, pygame.Color((0,0,0)), (x, y, __size[0], __size[1]), width=1)
                    font = pygame.font.Font('freesansbold.ttf', 10)
                    text = font.render(letter, True, (0,0,0))
                    self.__screen.blit(text, (x + 5, y + 5))
                    pygame.display.flip()

        
   
    def spawn_ai_ships(self, iValStart, iValEnd):
        arr = []
        for i in range(iValStart, iValEnd):    #loop for 5 ships
            for j in range(0,i+1):  #for length of ship
                if j == 0:                                             #if first square of ship
                    while True:                                        #loop until starting position isn't taken and the ship can be placed in bounds
                        randomStartingPoint = random.randint(0,64)
                        startPoint = self.__square_list[randomStartingPoint].getLocation()[1]
                        right = (int(startPoint[1]) + (len(self.ship_list[i])-1) <= 8)  #right is in bounds for length of ship
                        left  = (int(startPoint[1]) - (len(self.ship_list[i])-1) >= 1)  #left is in bounds for length of ship
                        down  = (ord(startPoint[0]) + (len(self.ship_list[i])-1) <=104) #down is in bounds for length of ship
                        up    = (ord(startPoint[0]) - (len(self.ship_list[i])-1) >=97)  #up is in bounds for length of ship

                        if (right or left or down or up) and self.__square_list[randomStartingPoint].getEmpty():
                            arr.append(startPoint)
                            self.ship_list[i][0] = startPoint
                            self.__square_list[randomStartingPoint].setEmpty(False)
                            break
                else:
                    while True:

                        if down:
                            nextPoint = str(chr(ord(startPoint[0]) + (j))) + str(startPoint[1])
                        elif right:
                            nextPoint = str(startPoint[0]) +  str(int(startPoint[1])+j)
                        elif left:
                            nextPoint = str(startPoint[0]) +  str(int(startPoint[1])-j)
                        elif up:
                            nextPoint = str(chr(ord(startPoint[0]) - (j))) + str(startPoint[1])
            
                        for square in range(0,64):
                            if self.__square_list[square].getLocation()[1] == nextPoint:
                                squareIndexValue = square
                                break
                    
                        if self.__square_list[squareIndexValue].getEmpty():
                            arr.append(nextPoint)
                            self.ship_list[i][j] = nextPoint
                            self.__square_list[squareIndexValue].setEmpty(False)
                            break
                        else:
                            for b in range(0, len(arr)):
                                for square in range(0,64):
                                    if self.__square_list[square].getLocation()[1] == arr[b]:
                                        squareIndexValue = square
                                        self.__square_list[square].setEmpty(True)
                                        break

                            if self.ship_list[4][4] != 'a' and self.ship_list[4][4] != '':
                                return

                            for x in range(0, len(self.ship_list[i])):
                                self.ship_list[i][x] = 'a'

                            if self.ship_list[i][0] == 'a':
                                self.spawn_ai_ships(i, (i+1))
                                pass

                            break  
                                       
            arr = []



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


