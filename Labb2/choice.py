import json
def readFile(filename, path = "./"):
    fileLocation = path + filename
    try:
        with open(fileLocation) as file_obj:
            content = file_obj.read()
            return content
    except FileNotFoundError as ferr:
        print(ferr)
        return None    
    