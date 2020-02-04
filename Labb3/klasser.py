import sys
import requests
import programm
class Choices():

    def __init__(self):
        def Meny(self):
            
            print("Välkommen till filmvärlden!")
            print("1. Sök efter en film: ")
            print("2. Historik")
            print("3. Avsluta")
            svar = input("Välj ett alternativ: ")
            
            while not svar == "":
                if svar == "1":
                    #searchMovie()
                    print("hej")
                    self.tillbaka()
                    break
                elif svar == "2":
                    print("hejdå")
                    self.tillbaka()
                    #visaHistorik()
                    break
                elif svar == "3":
                    sys.exit()
        Meny(self)  
    def tillbaka(self):
        svar = input("Vill du gå tillbaka till menyn? Y/N: ")
        if svar == "Yes" or svar == "y" or svar == "Y" or svar =="yes":
            programm.main()
            
            
            
                    
                    
    
