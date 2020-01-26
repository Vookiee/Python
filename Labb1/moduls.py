import random

def dela(x, y):
    for i in range(1,1000):
        if i % x == 0 and i % y == 0:
            print(i, end = ' ')

def gissaNummer():
    number = random.randint(1, 100)
    svar = int(input("\nSkriv in ett nummer mellan 1 och 100: "))
    tries = 1

    while True: 
        if number < svar:
            tries += 1
            svar = int(input("Skriv ett mindre tal: "))
            #error()
        elif number > svar:
            tries += 1
            svar = int(input("Skriv ett större tal: "))
           # error()
        else:
            print(f"Du gissade rätt! {svar} , det tog dig {tries} försök!")
            break
     
""" def error():
    if int(input("Skriv ett mindre tal: ")):
        try:
            svar =  int(input("Skriv ett heltal: "))
        except error:
            print("ERRROR! Skriv in ett heltal: ")
                       """