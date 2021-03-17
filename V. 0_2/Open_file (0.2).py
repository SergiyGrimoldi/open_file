#! /usr/bin/python
import glob
import os
login = []

#login_benvenuto
def benvenuto():
    print("\n\nBenvenuto nella gestione file")
    utente = input("Digitare nome utente ( o digitare 'EXIT' per chiudere il programma ): \n> ")
    #Aggiunge nome_utente alla lista login
    login.append(utente)
    
#Controllo se si vuole uscire
    if utente.lower() == "exit":
        exit()
        
        
    else:
        scelte()
        
def scelte():
    print("\n\nBenvenuto/a:","\n\n")
    
        #Cronologia utenti in base all'ora
    import time
    oggi = (time.strftime("%D--%H:%M:%S"))
    login.append(oggi)
        #Fine cronologia utenti in base all'ora
         
         
         
        #selezione di cosa si vuole fare
        # 1 - Leggere file esistente
        # 2 - Creare nuovo file
        # 3 - Scrivere su vecchio file
        # 8 - Mostra cartella file creati
        # 9 - Mostra ultimi acessi della sessione
        # 0 - Esci
    scelta = (input("Scegliere cosa fare: \n1 = Leggere un file esistente:\n2 = Creare nuovo file:\n3 = Scrivere vecchio file:\n\n8 = mostra cartella documenti:\n9 = mostra ultimi accessi della sessione:\n0 / EXIT = ritorna al login\n> "))
        
        #1
    if scelta == "1":
        open_old_file()
            
        #2    
    elif scelta == "2":
        new_file()
            
        #3
    elif scelta == "3":
        write_old_file()
            
        #8    
    elif scelta == "8":
        cronologia_files()
                
            
        #9
    elif scelta == "9":
        ultimi_accessi()
       
                
        #0        
    elif scelta == "0":
        benvenuto()
        
    elif scelta.lower() == "exit":
        benvenuto()
        
        #Fine selezione
            
#Fine controllo se si vuole uscire            
            




# 1
#vecchio_file_open
def open_old_file():
   
    file_open = input("> apri file esistente (inserire anche estensione file '.txt'): \n>")
    with open(file_open,"r") as file:
        for line in file:
            print(line)
    file.close()
    continuare()
 
 
#2    
#nuovo_file_create
def new_file():
    
    new_write = open(input("> Dai un nome al tuo nuovo file (inserire estensione file '.txt'): \n>"),"w")
    new_write.write(input("Scrivi nuova riga: "))
    new_write.write("\n")
    new_write.close()
    continuare()
 
 
    
#3    
#apro vecchio file in scrittura
def write_old_file():
    
    file_write = open(input("> apri file esistente (inserire estensione file '.txt'): \n>"),"a")
    file_write.write(input("Scrivi nuova riga: "))
    file_write.write("\n")
    file_write.close()
    continuare()
    

#logout
def continuare():
    print("\n\n")
    continuare_scelta = (input("Vuoi continuare?\n0 = no;\n1 = si;\n> "))
    if continuare_scelta == "0":
        benvenuto()
    elif continuare_scelta == "1":
        scelte()
            
            
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
    continuare()


def ultimi_accessi():
     with open('ultimi_accessi.txt', 'r') as dati:
            content = dati.read()
            print (content)
            dati.close()
            continuare()
    
#start
start = 1
while start:
    benvenuto()
    dati()
    continuare()
    
    
    
    