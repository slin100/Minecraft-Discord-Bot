
class FourWin:
    player1 = ""
    player2 = ""

    white = "⬜"
    black = "⬛"
    green = "🟩"
    red = "🟥"
    one = "1️⃣"
    two = "2️⃣"
    three = "3️⃣"
    four = "4️⃣"
    five = "5️⃣"
    six = "6️⃣"
    seven = "7️⃣"

    p1 = [white, white, white, white, white, white, white]
    p2 = [white, white, white, white, white, white, white]
    p3 = [white, white, white, white, white, white, white]
    p4 = [white, white, white, white, white, white, white]
    p5 = [white, white, white, white, white, white, white]
    p6 = [white, white, white, white, white, white, white]

    def MapText(self):
        plist = [self.p1,self.p2,self.p3,self.p4,self.p5,self.p6]
        FullMap = f"{self.one}{self.two}{self.three}{self.four}{self.five}{self.six}{self.seven}"
        num = -1
        for p in plist:
            num += 1
            FullMap += f"\n{p[0]}{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}"
        return FullMap
    
    def win(self, symb, x,y):
        winn = False
        # look wagerecht
        plist = [self.p1,self.p2,self.p3,self.p4,self.p5,self.p6]
        for p in plist:
            count = 0
            for i in range(6):
                if count >= 4:
                    winn = True
                if p[i]  == symb:
                    count += 1
                else:
                    count = 0
        # look vertical
        for i in range(6):
            count = 0
            for p in plist:
                if p[i]  == symb:
                    count += 1
                    if count >= 4:
                        winn = True
                else:
                    count = 0
        # look cross
        # /
        inRow = 1
        # Geht von unten links nach oben rechts
        try :
            if plist[y-1][x] == plist[y-2][x+1]:
                inRow += 1
                try:
                    if plist[y-3][x+2] == plist[y-2][x+1]:
                        inRow += 1
                        try:
                            if plist[y-3][x+2] == plist[y-4][x+3]:
                                inRow += 1
                        except: pass
                except: pass
        except: pass
        # Geht von oben rechts nach unten links
        try:
            if plist[y-1][x] == plist[y][x-1]:
                inRow += 1
                try:
                    if plist[y+1][x-2] == plist[y][x-1]:
                        inRow += 1
                        try:
                            if plist[y+1][x-2] == plist[y+2][x-3]:
                                inRow += 1
                        except: pass
                except: pass
        except: pass
        if inRow >= 4:
            winn = True
        
        # \
        inRow = 1
        # Geht von links nach unten rechts
        try:
            if plist[y-1][x] == plist[y][x+1]:
                inRow += 1
                try:
                    if plist[y+1][x+2] == plist[y-1][x]:
                        inRow += 1
                        try:
                            if plist[y+2][x+3] == plist[y][x+1]:
                                inRow += 1
                        except: pass
                except: pass
        except: pass

        # Geht von unten rechts nach oben links
        try:
            if plist[y-1][x] == plist[y-2][x-1]:
                inRow += 1
                try:
                    if plist[y-3][x-2] == plist[y-1][x]:
                        inRow += 1
                        try:
                            if plist[y-4][x-3] == plist[y-1][x]:
                                inRow += 1
                        except: pass
                except: pass
        except: pass
        if inRow >= 4:
            winn = True
        return winn




    def place(self, player, x:int):
        x = x - 1
        if str(player) == self.player1:
            symb = self.green
        elif str(player) == self.player2:
            symb = self.red

        if self.p6[x] != self.white:
            if self.p5[x] != self.white:
                if self.p4[x] != self.white:
                    if self.p3[x] != self.white:
                        if self.p2[x] != self.white:
                            if self.p1[x] != self.white:
                                return
                            else:
                                self.p1[x] = self.p1[x].replace(self.white, symb)
                                y = 1
                        else: 
                            self.p2[x] = self.p2[x].replace(self.white, symb)
                            y = 2
                    else: 
                        self.p3[x] = self.p3[x].replace(self.white, symb)
                        y = 3
                else: 
                    self.p4[x] = self.p4[x].replace(self.white, symb)
                    y = 4
            else: 
                self.p5[x] = self.p5[x].replace(self.white, symb)
                y = 5
        else: 
            self.p6[x] = self.p6[x].replace(self.white, symb)
            y = 6
        
        return self.win(symb,x,y)

if __name__ == "__main__":
    game = FourWin()
    game.player1 = "player name"
    game.player2 = "enemie name"
    Game = True
    while Game:
        content = input("Syntax = keyword+' '+ collum(ex. 4)")
        place_x = content.split(' ')[1]
        if game.place("player name", int(place_x)):
            Game = False
        FullMap = game.MapText()
        print(f"```{FullMap}```")