from tkinter import *


# procédure générale de déplacement :
def avance(gd, hb):
    global x1, y1
    x1, y1 = x1 + gd, y1 + hb
    can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)


# gestionnaires d'événements :
def depl_gauche():
    avance(-10, 0)
    print("gauche")


def depl_droite():
    avance(10, 0)
    print("droite")


def depl_haut():
    avance(0, -10)
    print("haut")


def depl_bas():
    avance(0, 10)
    print("bas")


# ------ Programme principal -------
print("main")
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10  # coordonnées initiales

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")

# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='blue', height=300, width=300)
oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, width=2, fill='green')
can1.pack(side=LEFT)
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
print("1")
Button(fen1, text='Gauche', command=depl_gauche).pack()
print("2")
Button(fen1, text='Droite', command=depl_droite).pack()
print("3")
Button(fen1, text='Haut', command=depl_haut).pack()
print("4")
Button(fen1, text='Bas', command=depl_bas).pack()
print("5")

# démarrage du réceptionnaire d'évènements (boucle principale) :
print("loop")
fen1.mainloop()
