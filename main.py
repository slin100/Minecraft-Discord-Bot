import datetime
import json
import time

import discord

from FourWinData import FourWin
from getData import getStatus, getTime
from TTTData import Game


class globalVar:
    ip = False
    debug = False
    time = 0
    delete = 60*60
    whitelist = []
    num = 0
    games = list()
    games_4Win = list()
    players = list()
    fourWinPlayers = list()

def serverInfo(update:bool=False, ip:str=False):
    status = json.dumps(getStatus(update=update, ip=ip), indent = 5)
    status = json.loads(status)
    if int(getTime(globalVar.time)) <= 0:
        globalVar.time = time.time()
    returnStatus = ""
    try:
        returnStatus = f'''
        Server status:   {status["online"]}
        Server IP:           {status["ip"]}
        Players online:  {status["players"]["online"]}
        Server version:  {status["version"]}
        Players:               {status["players"]["list"]}
        Next update in:    {int(getTime(globalVar.time)/60)} minutes {int(getTime(globalVar.time)%60)} seconds
        '''
    except TypeError:
        returnStatus = f'''
        Server status:   {status["online"]}
        Server IP:           {status["ip"]}
        Players online:  {status["players"]}
        Server version:  {status["version"]}
        Players:               {status["list"]}
        Next update in:    {int(getTime(globalVar.time)/60)} minutes {int(getTime(globalVar.time)%60)} seconds
        '''
    return returnStatus

def whitelist():
    with open("whitelist.txt", "r") as f:
            f = f.readlines()
            for i in f:
                globalVar.whitelist.append(i)

def timeNow():
    t = datetime.datetime.now().time()
    t = str(t).split(".")[0]
    return t

class MyClient(discord.Client):
    # logging in
    async def on_ready(self):
        whitelist()
        print(f"Whitelist:\n{globalVar.whitelist}")
        print("Ready")

    # on message
    async def on_message(self, message):
        if globalVar.debug:
            print(f"{message.author}----{message.content}")
        if message.author == client.user:
            return
        with open("log.txt", "a") as log:
            log.write(f"{message.author}----{message.channel}----{timeNow()}----{message.content}\n")
        
        if str(message.author)+"\n" not in globalVar.whitelist:
            await message.channel.send("You are not Whitelited\nPls contact the host if this is a misstake")
            return
        content = message.content


        '''Normal commands'''
        if content.lower() == "server":
            await message.channel.send(serverInfo(ip=globalVar.ip), delete_after=globalVar.delete)
            return

        if content.lower() == "help":
            await message.channel.send('''
            \n Get Server informations = server
            \n get help = help
            \nTicTacToe:
            \n  new game = new ttt [firstPlayer]:[secondPlayer]
            \n      example: new ttt [Max#0815]:[Mustermann#0017]
            \n  play the game = ttt x[num]:y[num]
            \n      example: ttt x1y3''')


        '''Tic Tac Toe'''
        if content.startswith("ttt"):
            content = content.split("ttt ")[1]
            x = content.split(":")[0]
            x = x.replace('x', '')
            y = content.split(":")[1]
            y = y.replace('y', '')
            x = int(x)
            y = int(y)
            for num, i in enumerate(globalVar.players):
                if str(message.author) in i:
                    gameNum = num
                    if str(message.author) == i[0]:
                        symb = "🟩"
                    elif str(message.author) == i[1]:
                        symb = "🟥"
                    else:
                        message.channel.send("Player not found")
                        return
            globalVar.games[gameNum].place(x, y, symb)
            print(globalVar.games[gameNum].printer())
            await message.channel.send(globalVar.games[gameNum].printer())
            if globalVar.games[gameNum].win(symb):
                await message.channel.send(str(message.author) + "won the game")
                del globalVar.games[gameNum]
                await message.channel.send("The game is now over")

        if content.startswith("new ttt"):
            content = content.split("new ttt ")[1]
            plyer1 = content.split(":")[0]
            plyer2 = content.split(":")[1]
            print(plyer1,plyer2)
            globalVar.players.append([plyer1,plyer2])
            game = Game()
            globalVar.games.append(game)
            await message.channel.send(f"New game was created for {plyer1} and {plyer2}")
            return
        

        '''FourWin'''
        if content.startswith("$4"):
            x = content.split("$4 ")[1]
            x = int(x)
            for num, i in enumerate(globalVar.fourWinPlayers):
                if str(message.author) in i:
                    gameNum = num
            print(globalVar.games_4Win)
            win = globalVar.games_4Win[gameNum].place(message.author, x)
            if win:
                del globalVar.games_4Win.game
                await message.channel.send("Game is over")
            FullMap = globalVar.games_4Win[gameNum].MapText()
            await message.channel.send(f"```{FullMap}```")
            
        if content.startswith("new 4win"):
            content = content.split("new 4win ")[1]
            plyer1 = content.split(":")[0]
            plyer2 = content.split(":")[1]
            print(plyer1,plyer2)
            globalVar.fourWinPlayers.append([plyer1,plyer2])
            game = FourWin()
            game.player1 = plyer1
            game.player2 = plyer2
            globalVar.games_4Win.append(game)
            await message.channel.send(f"New game was created for {plyer1} and {plyer2}")
            return

        '''Erweiterte Befehle'''
        if content.lower() == "server update":
            await message.channel.send(serverInfo(update=True,ip=globalVar.ip), delete_after=globalVar.delete)
            return

        if message.content.startswith("ip-update="):
            globalVar.ip = content.split("=")[1]
            print(globalVar.ip)
            await message.channel.send(serverInfo(ip=globalVar.ip), delete_after=globalVar.delete)
            return

        if content.startswith("whitelist.append") and str(message.author) == "Slin#0821":
            content = content.replace("whitelist.append(", "")
            content = content.replace(")", "")
            with open("whitelist.txt", "a") as f:
                f.write()
        if content.startswith("whitelist update"): whitelist()

        if content == "debug":
            if globalVar.debug:
                globalVar.debug = False
                globalVar.delete = 60*60
                return
            globalVar.debug = True
            globalVar.delete = 30
            return




if __name__ == '__main__':
    globalVar.time = time.time()
    print(serverInfo())

    client = MyClient()
    client.run("your--client--id")
