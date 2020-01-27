import choice
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
            choice.readFile('personer.csv', 'Python/Labb2/')
            tillbaka()
            break
        elif svar == "2":
            print("hej")
            tillbaka()
            break
        elif svar == "3": 
            print("hell") 
            tillbaka()
            break 
        elif svar == "4":
            print("abc")
            tillbaka()
            break
        elif svar == "5":  
            print("123")
            tillbaka()
        else: 
            break                       
      
def tillbaka():
    svar = input("Vill du gå tillbaka till menyn? Y/N: ")
    if svar == "Yes" or svar == "y" or svar == "Y":
        main()
           
             
main()

