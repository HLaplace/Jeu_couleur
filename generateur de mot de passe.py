from random import randint,choice
import string
from tkinter import *

# fonction de generation du mot de passe
def generation_mdp():
    # choix de toute les entités a mettre dans le mdp
    mdp = string.ascii_letters + string.digits + string.punctuation
    # definition du nombre de lettre a mettre dans le mdp
    password = "".join(choice(mdp) for x in range(randint(8, 16)))
    # remise a zero de la barre
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# creer la fenetre et toute ses info
window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.minsize(720, 480)
window.config(background="#A80A0E")

#creer la frame principale
frame = Frame(window, bg="#A80A0E")

#importation de l'image
width = 300
height = 300
#reglage de l'image
image = PhotoImage(file="password.png").zoom(18).subsample(32)       # image contenu dans le dossier ou est le code
canvas = Canvas(frame, width=width, height=height, bg="#A80A0E",bd=0,highlightthickness=0 )
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite a droite
right_frame = Frame(frame, bg="#A80A0E")

#creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Arial",20),bg="#A80A0E", fg="black")
label_title.pack()

#creer une box
password_entry = Entry(right_frame, font=("Arial",20),bg="#A80A0E", fg="black")
password_entry.pack()

#creer un bouton
generation_mdp_button = Button(right_frame, text="Générer", font=("Arial",20),bg="#A80A0E", fg="black",command=generation_mdp)
generation_mdp_button.pack(fill=X)

#on place la sous boite a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#afficher la frame
frame.pack(expand=YES)

# afficher la fenetre
window.mainloop()
