import json

# { finger : value, face : value, rfid : value, write : value }

def readfinger():
    return 1

def readface():
    return 1

def rfidIN():
    return 1

def rfidOUT():
    return 1

def write():
    entry = read()
    with open("data.json", 'r+') as file:
        data = json.load(file)
        data["users"].append(entry)
        file.seek(0)
        json.dump(data, file, indent=4)

def read():
    entry = {
        "finger" : readfinger(),
        "face"   : readface()  ,
        "rfidIN" : rfidIN()    ,
        "rfidOUT": rfidOUT()   ,
        "FLAG"   : 0
    }
    return entry

def authenticate() -> bool:
    entry = read()
    if entry["FLAG"] == 1:
        return False
    with open("data.json", 'r') as file:
        data = json.load(file)
        for user in range(data):
            if data[user] == entry:
                return True