import sys
import requests
import json

choice = []
last = []

class Choices():
    global choice

    def __init__(self):
        
        def tillbaka(self):
            svar = input("Vill du gå tillbaka till menyn? Y/N: ")
            if svar == "Yes" or svar == "y" or svar == "Y" or svar =="yes":
                Meny(self)
                
        def Meny(self):
            print("Välkommen till filmvärlden!")
            print("1. Sök efter en film: ")
            print("2. Historik")
            print("3. Avsluta")
            svar = input("Välj ett alternativ: ")
            
            while not svar == "":
                if svar == "1":
                    Api()
                    tillbaka(self)
                    break
                elif svar == "2":
                    print(f"Du har sökt på: {last}")
                    undermeny()
                    tillbaka(self)
                    #visaHistorik()
                    break
                elif svar == "3":
                    sys.exit()
        Meny(self)
        
class Api():
    global choice
    def __init__(self):
        def searchMovie(self):
            svar = input("1. Sök film: ")
            last.append(svar)
            movies = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=715f40c0&s={svar}')
            data = movies.json()
            try:
                with open('file.json', 'w',encoding="utf-8") as volkan:
                    w = json.dumps(data, ensure_ascii=False, indent=7)
                    volkan.write(w)
            except FileNotFoundError as error:
                print(error)
            values = data['Search'] 
            count = 0
            for i in values:
                count += 1
                print(count,i['Title'],i['Year'])   
        searchMovie(self)
        def chooseMovie(self):
            svar = int(input('1.1 Välj film: '))
            try:
                with open('file.json', encoding='utf-8') as volkan_json:
                    filmer = json.load(volkan_json)
                    val = filmer.get('Search')[svar-1]
                    choice.append(val['Title'])
                    
            except ValueError as error:
                print(error)
            try:
                with open('historik.json','w',encoding='utf-8') as savejson:
                   json.dump(val, savejson, ensure_ascii=False, indent = 7)
            except FileNotFoundError as ferror:
                print(ferror)          
        chooseMovie(self)        

class showHist():
    global choice
    def __init__(self):
        def visaHistorik(self):
            try:
                with open('historik.json','r',encoding='utf-8') as showjson:
                    data = json.load(showjson)
                    print(data)
            except FileNotFoundError as rerror:
                print(rerror)
        visaHistorik(self)

class undermeny():
    def __init__(self):
        def menyTwo(self):
            print("1. Visa info om senaste sökta filmer")
            print("2. Visa info om vald sökt film")
            print("3. Tillbaka till menyn")
            svar = input("Ditt val: ")  
            while not svar == "":
                if svar == "1":
                    print(choice)
                    menyTwo(self)
                    break
                elif svar == "2":
                    showHist()
                    menyTwo(self)
                    break
                elif svar == "3":
                    Choices()
        menyTwo(self)            
                    
                    
                 
                

        
                
