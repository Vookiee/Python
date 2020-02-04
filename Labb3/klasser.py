import sys
import requests
import json


class Choices():

    def __init__(self):
        
        def tillbaka(self):
            svar = input("Vill du gå tillbaka till menyn? Y/N: ")
            if svar == "Yes" or svar == "y" or svar == "Y" or svar =="yes":
                print("hej")
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
                    print("hejdå")
                    tillbaka(self)
                    # visaHistorik()
                    break
                elif svar == "3":
                    sys.exit()
        Meny(self)
        
class Api():
    def __init__(self):
        
        def searchMovie(self):
            svar = input("sök film: ")
            movies = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=715f40c0&s={svar}')
            data = movies.json()
            try:
                with open('file.json', 'w',encoding="utf-8") as volkan:
                    w = json.dumps(data, ensure_ascii=False, indent=7)
                    volkan.write(w)
                    print(w)
            except FileNotFoundError as error:
                print(error)
        searchMovie(self)
        def chooseMovie(self):
            svar = input('Välj film: ')
            try:
                with open('file.json') as volkan_json: 
                    
                    data = json.load(volkan_json)
                    for p in data:
                        if p["Search"] == svar:
                            print (p)
                        
            except ValueError as error:
                print(error)            
                    
        chooseMovie(self)        
                
        
                
