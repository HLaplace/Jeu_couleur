import tkinter as window

class Timer:
    def __init__(self, parent):

        self.seconds = 10
        self.label = window.Label(parent, text="10 s", font="Arial 30", width=10)
        self.label.pack()
        self.label.after(1000, self.refresh_label)

    def refresh_label(self):
        self.seconds -= 1
        self.label.configure(text="%i s" % self.seconds)
        self.label.after(1000, self.refresh_label)

        if self.seconds == 0:
            print("fini")
            exit()

if __name__ == "__main__":

    root = window.Tk()
    timer = Timer(root)
    root.mainloop()