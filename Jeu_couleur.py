import tkinter as tk
"update"
from tkinter import *
import random

class interface:

    def __init__(self):

        self.root = Tk()
        self.color = "#A2AFAD"
        self.root.title("Color game by HUGO")
        self.root.config(background=self.color)
        self.root.geometry("960x720")
        self.root.minsize(480, 360)
        self.score = 0
        self.definition_aleatoire()
        self.root.mainloop() # a mettre a la fin du __init__


    def definition_aleatoire(self):

        tab = [["Black", "red", "blue", "green", "purple", "orange", "yellow", "pink", "white"],
               ["Noir", "Rouge", "Bleu", "Vert", "Violet", "Orange", "Jaune", "Rose", "Blanc"],
               ["noir", "rouge", "bleu", "vert", "violet", "orange", "jaune", "rose", "blanc"]]

        self.rdm_valeur1 = (random.randint(0, 8))
        self.rdm_valeur2 = (random.randint(0, 8))

        # couleur du mot en fr maj
        self.var_temp = tab[1][self.rdm_valeur1]

        # couleur du mot en fr min
        self.var_temp_4 = tab[2][self.rdm_valeur1]

        # couleur du mot en anglais
        self.var_temp_2 = tab[0][self.rdm_valeur1]

        # mot
        self.var_temp_3 = tab[1][self.rdm_valeur2]

        self.inside_wdw()

    def inside_wdw(self):

        # créer frame
        self.frame = Frame(self.root, bg=self.color)
        self.frame.pack(expand=YES)

        # consigne
        self.label_consigne = Label(self.frame, text="Ecrivez la couleur du mot et pas le mot en lui même.", font=("Arial", 20),
                               fg="black", bg=self.color)
        self.label_consigne.pack(expand=YES)

        # Couleur
        self.label_title = Label(self.frame, text=self.var_temp_3, font=("Arial", 40), bg=self.color, fg=self.var_temp_2)
        self.label_title.pack(expand=YES)

        # suivi score
        self.label_score = Label(self.frame, text=self.score, font=("Arial", 20), fg="black", bg=self.color)
        self.label_score.pack(expand=YES)

        # barre de texte
        global saisie

        self.saisie = Entry(textvariable=StringVar(), width=20, justify=CENTER)
        self.saisie.focus_set()
        self.saisie.pack()

        self.root.bind('<Return>', self.callback)
        self.root.update()

    def fonction_verification(self):

        if self.zoneSaisie == self.var_temp or self.zoneSaisie == self.var_temp_4:
            print("ok couleur")
            self.label_consigne.destroy()
            self.frame.destroy()
            self.label_title.destroy()
            self.label_score.destroy()
            self.saisie.destroy()

            self.score = self.score + 1
            self.definition_aleatoire()

        else:
            print("perdu")
            exit()

    def callback(self,event):
        self.zoneSaisie = self.saisie.get()
        self.fonction_verification()

#--------------------Main--------------------

main = interface()
