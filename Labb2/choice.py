import json


def readFile(filename, path="./"):
    fileLocation = path + filename
    lines = []
    x= 0
    users = {
        "namn": " ",
        "Efternamn": " ",
        "Användarnamn": " ",
    }
    try:
        with open(fileLocation, encoding="utf-8") as file_obj:
            for line in file_obj:
                lines.append(line)
    except FileNotFoundError as ferr:
        print(ferr)
        return None

    for line in lines:
        print(line.rstrip("\n"))

    [x.split(";")[0] for x in lines]
    for x in users:
        users["namn"] = [x]

    [x.split(";")[1] for x in lines]
    for x in users:
        users["Efternamn"] = [x]

    [x.split(";")[2] for x in lines]
    for x in users:
        users["Användarnamn"] = [x]
        
    for x in lines:
        newList = [
            users
        ]
        print(newList)
