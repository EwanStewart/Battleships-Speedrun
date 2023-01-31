import pygame, sys
from board import Board
from square import Square
import pyautogui
import random

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

def create_buttons(screen):
    button_x_pos = 330
    button_y_pos = 300
    button_width = 150
    button_height = 25

    arr = ["first", "second", "third", "fourth", "fifth"]
    buttons = []

    for i in range(0,5):
        pygame.draw.rect(screen, pygame.Color((255,255,255)), (button_x_pos, button_y_pos, button_width, button_height))
        pygame.draw.rect(screen, pygame.Color((0,0,0)), (button_x_pos, button_y_pos, button_width, button_height), width=1)
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render("Place " + arr[i] + " ship (" +str(i+1) + " unit)", True, (0,0,0))
        center = (button_x_pos + 10)
        screen.blit(text, (center, button_y_pos+5))
        buttons.append(Square(button_x_pos, button_y_pos, i+1))
        button_y_pos +=50
        
    pygame.display.flip()
    return buttons

def check_button_clicked(buttons):
    mpos = pygame.mouse.get_pos() # Get mouse position
    for i in range(0, 5):
        if buttons[i] != None:
            square_x, square_y= buttons[i].getPosition()[0], buttons[i].getPosition()[1]
            if mpos[0] >=  square_x and mpos[0] <= square_x + 150:
                if mpos[1] >= square_y and mpos[1] <= square_y + 25:
                    return buttons[i].getLocation()[1]

    return False

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

def start(pBoard, cBoard):
    cBoard.spawn_ai_ships(0, 5)
    print(cBoard.ship_list)
    for ko in range(0, len(cBoard.ship_list)):
            colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))   #random colour for ship
            cBoard.set_square_colour(cBoard.ship_list[ko], colour)
    pass

def main():
    pygame.init()
    screen = create_window()
    player_board, computer_board = create_board(screen)
    buttons = create_buttons(screen)

    pre_game = True
    placing_ship = False
    ship_count = 0
    startGame = False
    temp = []
    buttonToggled = False
    start(player_board, computer_board)
    while True:
        for event in pygame.event.get():
            if not startGame:
                result = all_equal(buttons)
                if result:
                    startGame = True
                    start(player_board, computer_board)
            if event.type == pygame.MOUSEBUTTONUP:
                if pre_game:
                    if ship_count != 5:
                        buttonToggled = check_button_clicked(buttons) 
                        if buttonToggled:
                            pyautogui.alert("Please select " + str(buttonToggled) + " square(s) which are connected vertically or horizontally.")
                            pre_game = False
                            placing_ship = True
                    else:
                        pre_game = False
                        startGame = True
                elif placing_ship:
                    result = player_board.check_if_square_clicked()
                    if result:
                        if len(temp) < buttonToggled:
                            temp.append(result)
                            player_board.set_square_colour(temp, (255,0,0))
                            if len(temp) == buttonToggled:
                                player_board.ship_list[buttonToggled-1] = temp  #assign chosen square to board
                                x = buttons[buttonToggled-1].getLocation()[0][0]
                                y = buttons[buttonToggled-1].getLocation()[0][1]
                                buttons[buttonToggled-1] = None
                                pygame.draw.rect(screen, pygame.Color((255,0,0)), (x, y, 150, 25))  #cover over used button
                                pygame.display.flip()

                                temp = []
                                buttonToggled = False
                                placing_ship = False
                                pre_game = True
                else:
                    result = player_board.check_if_square_clicked()
                    if (result):
                        pass

            if event.type == pygame.QUIT: sys.exit()


if __name__ == "__main__":
    main()