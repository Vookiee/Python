def readFile():
    print ("hello")
    
def tillbaka():
    svar = input("Vill du gå tillbaka till menyn? Y/N")
    if svar == "Yes" or svar == "y" or svar == "Y":
        program.main()
    else:
        svar = 1