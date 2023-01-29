class Square:

    _empty: bool = True

    def __init__(self, x, y, letter):
        self.coord = x, y
        self.letter_location = letter
    
    def getLocation(self):
        return self.coord, self.letter_location


    