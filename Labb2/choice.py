import json


def readFile(filename, path="./"):
    fileLocation = path + filename
    lines = []
    users = []
    try:
        with open(fileLocation, encoding="utf-8") as file_obj:
            for line in file_obj:
                lines.append(line)
    except FileNotFoundError as ferr:
        print(ferr)
        return None

    for line in lines:
        print(line.rstrip("\n"))

    for x in lines:
        info = x.rstrip("\n").split(";")
        users.append({"namn": info[0],
                    "Efternamn": info[1],
                 "Användarnamn": info[2],
                     "Mail": info[3]})
    
    for x in users:
        print(x)

    # [x.split(";")[1] for x in lines]
    # for x in users:
    #     users["Efternamn"] = [x]

    # [x.split(";")[2] for x in lines]
    # for x in users:
    #     users["Användarnamn"] = [x]

    # for x in lines:
    #     newList = [
    #         users
    #     ]
    #     print(newList)
def savePersoner():
    