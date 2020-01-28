import json
users = []
lines = []

def readFile(filename, path="./"):
    fileLocation = path + filename
    try:
        with open(fileLocation, encoding="utf-8") as file_obj:
            for line in file_obj:
                lines.append(line)
    except FileNotFoundError as ferr:
        print(ferr)
        return None

    for x in lines:
        info = x.rstrip("\n").split(";")
        users.append({"namn": info[0],
                      "Efternamn": info[1],
                      "Användarnamn": info[2],
                      "Mail": info[3]})

    for x in users:
        print(x)
    return users

def savePersoner(filename):
    try:
        with open(filename, "w", encoding="utf-8") as saveP:   
            json.dump(users, saveP, ensure_ascii=False, indent=4)
    except FileNotFoundError as error:
        print(error)


def readPersoner(filename):
    try:
        with open(filename, "r", encoding="utf-8") as readP:
            lines = json.load(readP)
            return lines
    except FileNotFoundError as error:
        print(error)


def addPerson():
    namn = input("Skriv in nytt namn: ")
    enamn = input("Skriv in efternamn: ")
    user = input("Skriv in nytt användarnamn: ")
    mejl = input("Skriv in nytt mejl: ")
    users.append({
        "namn": namn,
        "Efternamn": enamn,
        "Användarnamn": user,
        "Mail": mejl
    })


def delPerson():
    user1 = input("Skriv in Efternamn du vill ta bort: ")
    for i in range(len(users)):
        if user1 == users[i]["Efternamn"]:
            del users[i]
            
        
