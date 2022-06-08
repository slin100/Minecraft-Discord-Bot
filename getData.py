import json
import requests
import time

def getIP():
    r = requests.get("https://what-is-my-ip.justyy.workers.dev/")
    return r.text.replace('"','')

def getStatus(update:bool=False, ip:str=False):
    if ip == False:
        ip = getIP()
    r = requests.get(f"https://api.mcsrvstat.us/2/{ip}")
    if update:
        r = requests.get(f"https://api.mcsrvstat.us/1/{ip}")
    j = json.loads(r.text)

    jData = ["online", "version", "players", "list", "ip"]

    returnData = '{ "online":"None", "ip":"None", "version":"No info", "players":"0", "list":"No one"}'
    returnData = json.loads(returnData)
    for data in jData:
        try:
            returnData[data] = j[data]
        except: pass
    return returnData

def getTime(GTime):
    tTime = time.time() - GTime
    if tTime > 10*60+10:
        GTime = time.time()
    timeLeft = 10*60+10 - tTime
    return int(timeLeft)


if __name__ == "__main__":
    print(getStatus())