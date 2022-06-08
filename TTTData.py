class Game:
    white = "⬜"
    one = "1️⃣"
    two = "2️⃣"
    three = "3️⃣"

    player_1 = None
    player_2 = None

    x1y1 = x2y1 = x3y1 = x1y2 = x2y2 = x3y2 = x1y3 = x2y3 = x3y3 = white

    def place(self, x ,y, symb):
        if y == 1:
            if x == 1 and self.x1y1 == self.white:
                self.x1y1 = symb
                return
            if x == 2 and self.x2y1 == self.white:
                self.x2y1 = symb
                return
            if x == 3 and self.x3y1 == self.white:
                self.x3y1 = symb
                return
        if y == 2:
            if x == 1 and self.x1y2 == self.white:
                self.x1y2 = symb
                return
            if x == 2 and self.x2y2 == self.white:
                self.x2y2 = symb
                return
            if x == 3 and self.x3y2 == self.white:
                self.x3y2 = symb
                return
        if y == 3:
            if x == 1 and self.x1y3 == self.white:
                self.x1y3 = symb
                return
            if x == 2 and self.x2y3 == self.white:
                self.x2y3 = symb
                return
            if x == 3 and self.x3y3 == self.white:
                self.x3y3 = symb
                return

    def win(self, symb):
        # Left to right
        if self.x1y1 == self.x2y1 == self.x3y1 == symb:
            return True
        if self.x1y2 == self.x2y2 == self.x3y2 == symb:
            return True
        if self.x1y3 == self.x2y3 == self.x3y3 == symb:
            return True
        # bottom to floor
        if self.x3y1 == self.x3y2 == self.x3y3 == symb:
            return True
        if self.x2y1 == self.x2y2 == self.x2y3 == symb:
            return True
        if self.x1y1 == self.x1y2 == self.x1y3 == symb:
            return True
        # corner mid corner
        if self.x1y1 == self.x2y2 == self.x3y3 == symb:
            return True
        if self.x3y1 == self.x2y2 == self.x1y3 == symb:
            return True
        return False
    
    def printer(self):
        self.gameBoard = f'''\n
  {self.one}{self.tow}{self.three}\n
{self.one}{self.x1y1}  {self.x2y1}  {self.x3y1}\n
{self.two}{self.x1y2}  {self.x2y2}  {self.x3y2}\n
{self.three}{self.x1y3}  {self.x2y3}  {self.x3y3}\n'''
        return self.gameBoard


