import tkinter as tk

from tkinter import *
from tkinter import filedialog as fd

#grafica

window = tk.Tk()
window.geometry("600x600")
window.title("Gestione file TXT")

window.resizable(False,False)
window.configure(background="white")


FPATH = None


TXT = tk.Text(window)
TXT.grid(sticky='nsew')


#funzioni


def apri():
    path = fd.askopenfilename(title='Scegli un file', filetypes=[("text", "*.txt"),('python', '*.py'),("tutti i file", "")])
    if len(path) > 0:
        global FPATH
        TXT.delete('1.0', 'end')
        with open(path, 'U') as f:
            TXT.insert('1.0', f.read())
        window.title(path)
        FPATH = path


def salva():
    if FPATH != None:
        with open(FPATH, 'w') as f:
            f.write(TXT.get('1.0', 'end'))

def nuovo():
    path = fd.asksaveasfilename(title='Dove Salvare')

    global FPATH
    with open(path, 'w') as f:
        f.write(TXT.get('1.0', 'end'))
    window.title(path)
    FPATH = path


def esci():
    exit()



#Pulsanti


#apri file
first_button = tk.Button(text="Apri vecchio file txt", command=apri,bg = "#71cf56")
first_button.grid(row=10, column=0, sticky="W")

#salva file
second_button = tk.Button(text="Salva", command=salva, bg="#13e3e1")
second_button.grid(row=11, column=0, sticky="W")

#nuovo file
third_button = tk.Button(text="Nuovo file txt", command=nuovo,bg="#FFD700")
third_button.grid(row=12, column=0, sticky="W")

#esci dal programma
exit_button = tk.Button(text="ESCI", command=esci, bg = "#FF6347")
exit_button.grid(row=14, column=0,sticky="w")


#finestra ricerca file
label_file_explorer = Label(window, text = "Gestione file TXT", width = 100, height = 4, fg = "blue")


#fine programms
if __name__ == "__main__":
    window.mainloop()
