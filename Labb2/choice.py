import json
users = []

def readFile(filename, path="./"):
    global users

    fileLocation = path + filename
    try:
        with open(fileLocation, encoding="utf-8") as personer:
            lines = personer.readlines()
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


def savePersoner(filename):
    try:
        with open(filename, "w", encoding="utf-8") as saveP:
            json.dump(users, saveP, ensure_ascii=False, indent=4)
    except FileNotFoundError as error:
        print(error)


def readPersoner(filename):
    global users
    try:
        with open(filename, encoding="utf-8") as readP:
            users = json.load(readP)
            return users

    except FileNotFoundError as error:
        print(error)


def addPerson():
    global users
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
            break
