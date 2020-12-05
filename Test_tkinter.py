from tkinter import *

# créer la fenetre
window = Tk()

def fonction():

    global valeur
    valeur = saisir.get()
    print(valeur)

# personnalisation fenetre
window.title("Ma fenetre") #titre de la fenetre
window.geometry("960x720") # taille de base
window.minsize(480 ,360)   # taille minimale
window.config(background='#F37C00') # choisi la couleur du fond

#titre en plein milieu
label_title = Label(window, text = "bienvenue sur l'application",
                    font=("Arial", 40),bg="#F37C00",fg="white") # créer un texte avec
# sa police,sa taille de caractére la couleur du carré et du texte
label_title.pack(expand = YES) # affiche le texte précédement créer avec en paramétre
#le fait qu'il soit toujour au centre

# barre de texte
saisir=StringVar() # prevoir la variable pour recevoir le texte saisi
saisir.set("Nom ?")
saisie=Entry(textvariable=saisir, width=10,justify=CENTER)
saisie.pack()

bouton=Button(window, text="Validez", command=fonction)
bouton.pack()

# afficher la fenetre
window.mainloop()

