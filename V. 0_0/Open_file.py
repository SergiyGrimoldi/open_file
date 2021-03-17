#! /usr/bin/python
import glob
import os
login = []



#vecchio_file_open
def open_old_file():

    lista_old = open(input("> apri file esistente (inserire estensione file '.txt'): \n>"))
    content_old = lista_old.read()
    print("\n\n")
    print(content_old)
    print("\n\n")
    lista_old.close()
    continuare()
    
    
#apro file in scrittura
def write_old_file():
    lista_write = open(input("> apri file esistente (inserire estensione file '.txt'): \n>"),"a")
    
    lista_write.write(input("Scrivi nuova riga: "))
    lista_write.write("\n")
    lista_write.close()
    continuare()
    
    
#nuvo_file_create
def new_file():
    new_file = open(input("inserire nome file seguito da '.txt': "),"w")
    
    new_file.close()
    continuare()
    
    
#nuovo_file_open_write
def open_new_file():
    lista = open(input("> dare un nome al nuovo file (inserire estensione file '.txt'): \n>"))
    content = lista.read()
    
    print("\n\n")
    print(content)
    print("\n\n")
    lista.close()
    continuare()

    
    
    
#login_benvenuto
def benvenuto():
    print("\n\nBenvenuto nella gestione file")
    utente = input("Digitare nome utente ( o digitare 'EXIT' per chiudere il programma ): \n> ")
    
    
    if utente.lower() == "exit":
        exit()
    else:
        print("\n\nBenvenuto: ", utente, "\n\n")
        login.append(utente)
        import time
        oggi = (time.strftime("%D--%H:%M:%S"))
        login.append(oggi)
        
         
        scelta = int(input("Scegliere cosa fare: \n1 = Leggere un file esistente:\n2 = Scrivere nuovo file:\n3 = Scrivere vecchio file:\n\n8 = mostra cartella documenti:\n9 = mostra ultimi accessi della sessione:\n0 = ritorna al login\n> "))
        if scelta == 1:
            open_old_file()
        elif scelta == 2:
            new_file()
        elif scelta == 3:
            write_old_file()
        elif scelta == 9:
            with open('ultimi_accessi.txt', 'r') as dati:
                content = dati.read()
                print (content)
                dati.close()
        elif scelta == 0:
            benvenuto()
        elif scelta == 8:
            cronologia_files()
            continuare()
            
            
#logout
def continuare():
    print("\n\n")
    continuare = (input("Vuoi continuare?\n0 = no;\n1 = si;\n> "))
    if continuare == 0:
        benvenuto()
    elif continuare == 1:
        scelta = int(input("Scegliere cosa fare: \n1 = Leggere un file esistente:\n2 = Scrivere nuovo file:\n3 = Scrivere vecchio file:\n\n8 = mostra cartella documenti:\n9 = mostra ultimo accesso per sessione:\n0 = ritorna al login\n> "))
        if scelta == 1:
            open_old_file()
            dati()
        elif scelta == 2:
            new_file()
            dati()
        elif scelta == 3:
            write_old_file()
            dati()
        elif scelta == 9:
            print(login)
        elif scelta == 0:
            benvenuto()
        elif scelta == 8:
            cronologia_files()
            dati()
            continuare()
            
            
#cronologia_utenti           
def dati():
    with open('ultimi_accessi.txt', 'a') as dati:
        for utenti in login:
            dati.write(" - %s\n" % utenti)
        dati.close()
        
        
#cronologia_file        
def cronologia_files():
    files = glob.glob("*.txt")
    files.sort(key=os.path.getmtime, reverse=True)
    for file in files:
        print(file)

    
#start
start = 1
while start:
    benvenuto()
    dati()
    continuare()
    
    
    
    