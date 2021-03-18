  # Programma di Sergiy Grimoldi
  # 2_0

######################################### import #########################################

import tkinter as tk # grafica
from tkinter import * # grafica
from tkinter import ttk # grafica
from tkinter import scrolledtext # grafica - per text box scrolling

import os # per trovare cartella di sistema 
from tkinter import filedialog as fd # per richiesta directory di salvataggio

import time # per cronologia utenti in file - login.txt

######################################### import #########################################



def login_main(): # Finestra di login

   
    login = tk.Tk() 
    login.geometry('200x110')
    login.title("Login")

    login.resizable(False,False)



    def next():
        
        def login_file(): # cronologia utenti in file - login.txt
    
            login_list = []


            nome = entryNome.get()
            cognome = entryCognome.get()
            
            login_list.append(nome)
            login_list.append(cognome)
            


            with open("Login.txt", "a")as login_txt :
                login_txt.write("\n-------------------------------------------------------------------------------------------------\n")
                data_ora = (time.strftime("    %D    %H:%M:%S   "))
                login_txt.write(data_ora)
                for utenti in login_list:
                    login_txt.write(" ")
                    login_txt.write(utenti)
                login_txt.close()
                
        login_file()

        login.destroy()
        second_window()
        

    def close_login():
        login.destroy()

    labelNome = tk.Label(login, text = "Nome")
    labelNome.grid(column=0, row=0, sticky=tk.W)

    labelCognome = tk.Label(login, text = "Cognome")
    labelCognome.grid(column=0, row=1, sticky=tk.W)

    nomeString = tk.StringVar()
    cognomeString = tk.StringVar()


    entryNome = tk.Entry(login, width=20, textvariable=nomeString)
    entryNome.grid(column=1, row=0, padx=10)

    entryCognome = tk.Entry(login, width=20, textvariable=cognomeString)
    entryCognome.grid(column=1, row=1, padx=10)


    loginButton = tk.Button(login, text = 'LOGIN', command=next)
    loginButton.grid(column=1, row=2, sticky=tk.W)

    closeButton = tk.Button(login, text = 'EXIT', command=close_login)
    closeButton.grid(column=1, row=3, sticky=tk.W)

    login.mainloop()



def main_window(): # Finestra Editor TXT

    
    main_window = tk.Tk()
    main_window.geometry('900x600')
    main_window.title("TXT - Edit")
    main_window.resizable(False, False)


    rows = 0
    while rows < 10:
        main_window.rowconfigure(rows, weight=1)
        main_window.columnconfigure(rows, weight=1)
        rows+=1



    Text_box = scrolledtext.ScrolledText(main_window)
    Text_box.grid(row=4,column=2)


    ######### Inizializzazione StatusBar #########

    statusbar = StringVar()
    statusbar.set("Benvenuto")
    sbar = Label(main_window, textvariable=statusbar, relief=SUNKEN, anchor="w")
    sbar.grid(row=20, column=0,sticky=tk.S)

    
    def bar_salvato():
        statusbar.set("Sto salvando...")
        sbar.update()
        import time
        time.sleep(1)
        statusbar.set("Salvato")

    def bar_aperto():
        statusbar.set("Sto Aprendo...")
        sbar.update()
        import time
        time.sleep(1)
        statusbar.set("Aperto")

    def bar_creato():
        statusbar.set("Sto creando...")
        sbar.update()
        import time
        time.sleep(1)
        statusbar.set("Creato")
        
        
    ######### Termino StatusBar #########

    def buttons_main():
        
        FPATH = None


        #### apri file ####
        def old_file():
            path = fd.askopenfilename(title='Scegli un file', filetypes=[("text", "*.txt"),("tutti i file", ""),("pdf","*pdf")])
            if len(path) > 0:
                global FPATH
                Text_box.delete('1.0', 'end')
                with open(path, 'U') as f:
                    Text_box.insert('1.0', f.read())
                main_window.title(path)
                FPATH = path
            bar_aperto()
        ## pulsante ##
        open_button = tk.Button(main_window, text="Apri vecchio file", command=old_file)
        open_button.grid(row=0,column=0, sticky=tk.NW, pady=5, padx=5)
        ## pulsante ##
        #### apri file ####


        #### crea file ####
        def create():

            Text_box.delete("1.0","end")
            path = fd.asksaveasfilename(title='Dove Creare', defaultextension=".txt")

            global FPATH
            with open(path, 'w') as f:
                f.write(Text_box.get('1.0', 'end'))
            main_window.title(path)
            FPATH = path
            bar_creato()
        ## pulsante ##
        create_button = tk.Button(main_window, text="Crea nuovo file",command=create)
        create_button.grid(row=0,column=1, sticky=tk.NW, pady=5, padx=5)
        ## pulsante ##
        #### crea file ####


        #### salva file ####
        def save_file():

            global FPATH
            with open(FPATH, 'w') as f:
                f.write(Text_box.get('1.0', 'end'))
            bar_salvato()
        ## pulsante ##
        save_button = tk.Button(main_window, text="Salva file", command=save_file)
        save_button.grid(row=0,column=2, sticky=tk.NW, pady=5, padx=5)
        ## pulsante ##
        #### salva file ####


        #### salva con nome ####
        def save_file_as():
            path = fd.asksaveasfilename(title='Dove Salvare', defaultextension=".txt")

            global FPATH
            with open(path, 'w') as f:
                f.write(Text_box.get('1.0', 'end'))
            app.title(path)
            FPATH = path
            bar_creato()
        ## pulsante ##
        save_as_button = tk.Button(main_window, text="Salva con nome",command=save_file_as)
        save_as_button.grid(row=0,column=3, sticky=tk.NW, pady=5, padx=5)
        ## pulsante ##
        #### salva con nome ####

        #### esci ####
        def close_main_window():
            main_window.destroy()
        ## pulsante ##
        close_button = tk.Button(main_window, text="Esci", command=close_main_window)
        close_button.grid(row=0,column=4, sticky=tk.NE, pady=5, padx=5)
        ## pulsante ##
        #### esci ####


        
    
    
    buttons_main()

    

    ##### Fine MainWindow #####

    main_window.mainloop()

    ##### Fine MainWindow #####



def second_window():

    def next_1():
        second_window.destroy()
        main_window()
    def exit_second_window():
        second_window.destroy()
        login_main()

    second_window=tk.Tk()
    second_window.geometry("500x500")
    second_window.title("Prova")
    
    select_button = tk.Button(second_window, text="TXT - EDIT", command=next_1)
    select_button.place(x=23,y=23)

    select_button_2 = tk.Button(second_window, text="TORNA AL LOGIN", command=exit_second_window)
    select_button_2.place(x=23, y=53)

    second_window.mainloop()



######################################### ESEGUI #########################################


login_main()
second_window()


######################################### ESEGUI #########################################