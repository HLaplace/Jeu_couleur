from tkinter import *
import random

score = 0

def callback(event):
    fonction()
    window.destroy()

def fonction():

    global score

    zoneSaisie = saisie.get()

    if zoneSaisie == var_temp or zoneSaisie == var_temp_4:
        print("ok couleur")
        score = score + 1
        return True

    else:
        print("perdu")
        print(score)
        exit()

def main():

    global saisie,var_temp_4
    global var_temp,window

    tab = [["Black", "red", "blue", "green", "purple", "orange", "yellow", "pink","white"],
           ["Noir","Rouge","Bleu","Vert","Violet","Orange","Jaune","Rose","Blanc"],
           ["noir","rouge","bleu","vert","violet","orange","jaune","rose","blanc"]]

    rdm_valeur1 = (random.randint(0, 8))
    rdm_valeur2 = (random.randint(0, 8))

    #couleur du mot en fr maj
    var_temp = tab[1][rdm_valeur1]

    # couleur du mot en fr min
    var_temp_4 = tab[2][rdm_valeur1]

    #couleur du mot en anglais
    var_temp_2 = tab[0][rdm_valeur1]

    #mot
    var_temp_3 = tab[1][rdm_valeur2]

    # Fenetre
    window = Tk()
    window.title("Color game by HUGO")  # titre de la fenetre
    window.geometry("960x720")  # taille de base
    window.minsize(480, 360)  # taille minimale
    window.config(background="#A2AFAD")  # choisi la couleur du fond
    print("fenetre")

    # créer frame
    frame = Frame(window, bg="#A2AFAD")
    frame.pack(expand=YES)

    # Consigne
    label_consigne = Label(frame,text="Ecrivez la couleur du mot et pas le mot en lui même.",font=("Arial", 20),fg="black",bg="#A2AFAD")
    label_consigne.pack(expand=YES)

    # Couleur
    label_title = Label(frame,text=var_temp_3,font=("Arial", 40),bg="#A2AFAD",fg=var_temp_2)
    label_title.pack(expand=YES)

    # suivi score
    label_score = Label(frame,text=score,font=("Arial", 20),fg="black",bg="#A2AFAD")
    label_score.pack(expand=YES)

    # barre de texte
    saisie = Entry(textvariable=StringVar(), width=20, justify=CENTER)
    saisie.pack()
    saisie.focus_set()

    # Retour avec entree
    window.bind('<Return>', callback)
    window.mainloop()

#--------------------Main--------------------
while fonction != True:

    main()


