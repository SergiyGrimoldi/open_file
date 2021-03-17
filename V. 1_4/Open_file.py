import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkdocviewer import *
from tkinter import ttk



def text():

    login.destroy()


        #finestra app
    app = tk.Tk()
    app.geometry('900x800')
    app.title("(TXT)  Manager")

    app.resizable(False,False)
    app.configure(background="white")


        #statusbar
    statusvar = StringVar()
    statusvar.set("Benvenuto - Prima di scrivere Crea un nuovo file o aprine uno vecchio")
    sbar = Label(app, textvariable=statusvar, relief=SUNKEN, anchor="w")
    sbar.pack(side=BOTTOM, fill=X)


        #casella di testo scorrevole
    Text_box = scrolledtext.ScrolledText(app,width=97,height=40)
    Text_box.pack(pady=10, padx=10)


        #funzioni
    FPATH = None


        #apri file
    def old_file():
        path = fd.askopenfilename(title='Scegli un file', filetypes=[("text", "*.txt"),("tutti i file", ""),("pdf","*pdf")])
        if len(path) > 0:
            global FPATH
            Text_box.delete('1.0', 'end')
            with open(path, 'U') as f:
                Text_box.insert('1.0', f.read())
            app.title(path)
            FPATH = path
            bar_aperto()


            #salva file
    def save_file():
        with open(FPATH, 'w') as f:
                f.write(Text_box.get('1.0', 'end'))
                bar_salvato()


            #salva con nome
    def save_file_as():
        path = fd.asksaveasfilename(title='Dove Salvare', defaultextension=".txt")

        global FPATH
        with open(path, 'w') as f:
            f.write(Text_box.get('1.0', 'end'))
        app.title(path)
        FPATH = path
        bar_creato()


            #aggiornamento barra di stato
    def bar_salvato():
        statusvar.set("Sto salvando...")
        sbar.update()
        import time
        time.sleep(1)
        statusvar.set("Salvato")

    def bar_aperto():
        statusvar.set("Sto Aprendo...")
        sbar.update()
        import time
        time.sleep(1)
        statusvar.set("Aperto")

    def bar_creato():
        statusvar.set("Sto creando...")
        sbar.update()
        import time
        time.sleep(1)
        statusvar.set("Creato")
        statusvar.set("Elimina il testo se di un vecchio file - Clicca su salva se lo avevi scrittpo prima di fare 'salva con nome', altrimenti perdi il lavoro fatto")

        #close windows - fine programma

    def close_window():

        # Create a DocViewer widget
        app.destroy()
        


            #pulsanti left
        # Open_old_file
    button1 = tk.Button(app, text="Apri vecchio file", command=old_file)
    button1.pack(side=tk.LEFT, padx=5)


        #Create_new_file
    button3 = tk.Button(app, text="Crea nuovo file", command=save_file_as)
    button3.pack(side=tk.LEFT, padx=5)


        #CLOSE windows 1
    button5 = tk.Button(app, text="CLOSE", command=close_window)
    button5.pack(side=tk.LEFT, padx=150)


        #pulsanti right
        #Save_file_as
    button2 = tk.Button(app, text="Salva con nome", command=save_file_as)
    button2.pack(side=tk.RIGHT, padx=5)


        #Save_file
    button4 = tk.Button(app, text="Salva", command=save_file)
    button4.pack(side=tk.RIGHT, padx=5)


    app.mainloop()




###########################################################################   Inizio Login  ######################################################################
login = tk.Tk() 
login.geometry('200x110')

def close_login():
    login.destroy()


labelNome = tk.Label(login, text = "Nome")
labelNome.grid(column=0, row=0, sticky=tk.W)
labelCognome = tk.Label(login, text = "Cognome")
labelCognome.grid(column=0, row=1, sticky=tk.W)
login_list = []

nomeString = tk.StringVar()

cognomeString = tk.StringVar()


entryNome = tk.Entry(login, width=20, textvariable=nomeString)
entryNome.grid(column=1, row=0, padx=10)
nome = entryNome.get()
login_list.append(nome)


entryCognome = tk.Entry(login, width=20, textvariable=cognomeString)
entryCognome.grid(column=1, row=1, padx=10)
cognome = entryCognome.get()
login_list.append(cognome)



with open("Login.txt", "a") as login_txt:
    for utenti in login_list:
        login_txt.write(utenti)
        print(utenti)


resultButton = tk.Button(login, text = 'LOGIN', command=text)
resultButton.grid(column=1, row=2, sticky=tk.W)

closeButton = tk.Button(login, text = 'EXIT', command=close_login)
closeButton.grid(column=1, row=3, sticky=tk.W)

login.mainloop()

###########################################################################   Fine Login  ######################################################################