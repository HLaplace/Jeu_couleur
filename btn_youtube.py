# Bouton youtube "code propre"

from tkinter import *
import webbrowser

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        #self.window.iconbitmap("logo.ico")
        self.window.config(background='#41B77F')

        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_youtube_button()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Go ytb", font=("Courrier", 25), bg='#41B77F',
                               fg='white')
        label_subtitle.pack()

    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Ouvrir Youtube", font=("Courrier", 25), bg='white', fg='#41B77F',
                           command=self.open_ytb)
        yt_button.pack(pady=25, fill=X)

    def open_ytb(self):
        webbrowser.open_new("https://www.youtube.com/")

# afficher
app = MyApp()
app.window.mainloop()