import tkinter as tk

from tkinter import *
from tkinter import filedialog as fd



#grafica

window = tk.Tk()
window.geometry("600x600")
window.title("Gestione file di testo")
window.pack()

statusbar = tk.Label(window, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

window.resizable(False,False)
window.configure(background="white")

try:
    bg = PhotoImage(file = "image.png")

    label1 = Label(window, image=bg)
    label1.place(x=0,y=0)
    FPATH = None

except:
    print("Tutto ok ma non riesco a recuperare lo sfondo dell'app")

Text_box = tk.Text(window)
Text_box.grid()


#funzioni

def apri():
    path = fd.askopenfilename(title='Scegli un file', filetypes=[("text", "*.txt"),("tutti i file", ""),("pdf","*pdf")])
    if len(path) > 0:
        global FPATH
        Text_box.delete('1.0', 'end')
        with open(path, 'U') as f:
            Text_box.insert('1.0', f.read())
        window.title(path)
        FPATH = path


def salva():
    if FPATH != None:
        with open(FPATH, 'w') as f:
            f.write(Text_box.get('1.0', 'end'))

def nuovo():
    path = fd.asksaveasfilename(title='Dove Salvare', defaultextension=".txt")

    global FPATH
    with open(path, 'w') as f:
        f.write(Text_box.get('1.0', 'end'))
    window.title(path)
    FPATH = path


def esci():
    exit()

def Work_in_progress():
    print("working")

#Pulsanti


#apri file
first_button = tk.Button(text="Apri vecchio file txt", command=apri,bg = "#71cf56")
first_button.grid(row=10, column=0, sticky="W")

#salva file
second_button = tk.Button(text="Salva", command=salva, bg="#13e3e1")
second_button.grid(row=11, column=0, sticky="W")

#nuovo file
fourth_button = tk.Button(text="Nuovo file txt", command=nuovo,bg="#FFD700")
fourth_button.grid(row=13, column=0, sticky="W")

#esci dal programma
exit_button = tk.Button(text="ESCI", command=esci, bg = "#FF6347")
exit_button.grid(row=14, column=0,sticky="w")


#finestra ricerca file
label_file_explorer = Label(window, text = "Gestione file TXT", width = 100, height = 4, fg = "blue")


#fine programms
if __name__ == "__main__":
    window.mainloop()
