import sys
import requests
import json

choice = []
last = []

class Choices():
    global choice

    def __init__(self):
        self.Meny()
        
    def tillbaka(self):
        svar = input("Vill du gå tillbaka till menyn? Y/N: ")
        if svar == "Yes" or svar == "y" or svar == "Y" or svar =="yes":
            self.Meny()
            
    def Meny(self):
        print("Välkommen till filmvärlden!")
        print("1. Sök efter en film: ")
        print("2. Historik")
        print("3. Avsluta")
        svar = input("Välj ett alternativ: ")
        print("\n")
        
        while not svar == "":
            if svar == "1":
                Api()
                self.tillbaka()
                break
            elif svar == "2":
                print(f"Du har sökt på: {last}")
                undermeny()
                self.tillbaka()
                break
            elif svar == "3":
                sys.exit()
        
class Api():
    global choice
    def __init__(self):
        self.searchMovie()
        self.chooseMovie()
        
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
        try:
            values = data['Search']
            count = 0
            for i in values:
                count += 1
                print(count,i['Title'],i['Year']) 
        except KeyError as error:
            print('ingen film hittades')
        
    def chooseMovie(self):
        svar = int(input('1.1 Välj film: '))
        print("\n")
        try:
            with open('file.json', encoding='utf-8') as volkan_json:
                filmer = json.load(volkan_json)
                val = filmer.get('Search')[svar-1]
                print(f"Title: {val['Title']}")
                print(f"Year: {val['Year']}")
                print(f"Type: {val['Type']}")
                print(f"Poster: {val['Poster']}\n")
                choice.append(val)
                
        except ValueError as error:
            print(error)
        try:
            with open('historik.json','w',encoding='utf-8') as savejson:
                json.dump(choice, savejson, ensure_ascii=False, indent = 7)
        except FileNotFoundError as ferror:
            print(ferror)          

class showHist():
    global choice
    def __init__(self):
        self.visaHistorik()
    def visaHistorik(self):
        try:
            with open('historik.json','r',encoding='utf-8') as showjson:
                data = json.load(showjson)
                print(data)
        except FileNotFoundError as rerror:
            print(rerror)

class undermeny():
    global choice
    def __init__(self):
        self.menyTwo()
        
    def menyTwo(self):
        print("1. Visa info om senaste sökta filmer")
        print("2. Tillbaka till menyn")
        print("\n")
        svar = input("Ditt val: ")  
        while not svar == "":
            if svar == "1":
                uVal()
                self.menyTwo()
                break
            elif svar == "2":
                Choices()
class uVal():
    def __init__(self):
        self.underVal()
        
    def underVal(self):
        try:
            with open('historik.json',encoding="utf-8") as volkan:
                read = json.load(volkan)
                
                count = 0
                for i in read:
                    count += 1
                    print(count,i['Title'],i['Year'])
                svar = int(input("Välj film för mer info: "))
                print("\n")
                val = read[svar-1]['imdbID']
                movies = requests.get(f'http://www.omdbapi.com/?apikey=715f40c0&i={val}')
                data = movies.json()
                print(f"Title: {data['Title']}")
                print(f"Year: {data['Year']}")
                print(f"Released: {data['Released']}")
                print(f"Length: {data['Runtime']}")
                print(f"Genre: {data['Genre']}")
                print(f"Actors: {data['Actors']}")
                print(f"Plot: {data['Plot']}")
                print(f"Type: {data['Type']}")
                print(f"Poster: {data['Poster']}\n")
                
                
                
        except FileNotFoundError as error:
            print(error)       
            
                    
                    
                    
                 
                

        
                
