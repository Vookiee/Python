import choice
import sys
def main ():
    meny()
    
    
def meny ():
    print("Välkommen!")
    print("1. Läs in fil ")
    print("2. Visa json-data")
    print("3. Lägg till person")
    print("4. Ta bort person")
    print("5. Spara fil")
    print("6. Avsluta")
    svar = input("Välj ett alternativ: ")
    while not svar == "":
        if svar == "1":
            choice.readFile('personer.csv', 'files/')
            
            tillbaka()
            break
        elif svar == "2":
            visa = choice.readPersoner('personer.json')
            print(visa)
            choice.savePersoner('personer.json')
            tillbaka()
            break
        elif svar == "3": 
            choice.addPerson()
            tillbaka()
            break 
        elif svar == "4":
            choice.delPerson()
            choice.savePersoner('personer.json')
            tillbaka()
            break
        elif svar == "5":  
            choice.savePersoner('personer.json')
            tillbaka()
        elif svar == "6": 
            sys.exit()                    
      
def tillbaka():
    svar = input("Vill du gå tillbaka till menyn? Y/N: ")
    if svar == "Yes" or svar == "y" or svar == "Y" or svar =="yes":
        main()
    else:
        sys.exit()
        
           
             
main()

