from tkinter import *

class interface:

    def __init__(self):

        self.root = Tk()
        self.color = "#A2AFAD"
        self.root.title("Color game by HUGO")
        self.root.config(background=self.color)
        self.root.geometry("960x720")
        self.root.minsize(480, 360)

        self.saisie = Entry(textvariable=StringVar(), width=20, justify=CENTER)
        self.saisie.focus_set()
        self.saisie.pack()

        self.root.bind('<Return>', callback)
        self.root.mainloop() # a mettre a la fin du __init__

def fonc_test():
    print(zoneSaisie)

def callback(self, event):
    zoneSaisie = saisie.get()
    fonc_test()

main = interface()