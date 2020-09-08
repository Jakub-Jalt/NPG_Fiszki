import tkinter as tk
from tkinter import messagebox as msb
import tryby
import config

checkback = 0


class App:

    def __init__(self, root):
        self.root = root
        self.main()

###############################################################################
    #########################      1        ########################
###############################################################################
    def main(self):

        config.page = 1

        self.label_name = tk.StringVar()
        self.label1 = tk.Label(self.root, font=80, textvariable=self.label_name).place(relx=0.1, rely=0.2, relwidth=0.8)

        self.label_name.set("Witaj w aplikacji do nauki \n poprzez Fiszki !!! \n\n podaj swoje imie: ")

        self.name = tk.Entry(self.root)
        self.name.place(relx=0.25, rely=0.4, relwidth=0.3)

        self.button_ok = tk.Button(self.root, width=10, text="OK", command=lambda: hello(self.name.get()))
        self.button_ok.place(relx=0.6, rely=0.4, relwidth=0.15)

        def hello(name):
            if name == "":
                msb.showinfo("info", 'Podaj imie !!!')
            else:
                print(str)
                msb.showinfo("info", 'Witaj, {0}\n teraz czeka cię nauka :)'.format(name))
                config.nick = name  # przypisanie imienia do zmiennej globalnej
                self.button_ok.destroy()
                self.name.destroy()
                self.choostyppage()

###############################################################################
      #########################      2        ########################
###############################################################################
    def choostyppage(self):

        config.page = 2

        self.label_name.set("WYBIERZ TRYB: ")

        def type1():  # nauka
            config.typechoos = 1
            self.button_learning.destroy()
            self.button_writing.destroy()
            self.button_stats.destroy()
            self.choosgamepage()

        def type2():  # wpisywanie
            config.typechoos = 2
            self.button_writing.destroy()
            self.button_learning.destroy()
            self.button_stats.destroy()
            self.choosgamepage()

        self.button_learning = tk.Button(self.root, text="NAUKA", command=type1, width=15)
        self.button_writing = tk.Button(self.root, text="WYPISYWANIE", command=type2, width=15)
        self.button_stats = tk.Button(self.root, text="Statystyki", width=15)  ## BRAK KOMENDY !!!
        self.button_learning.place(relx=0.35, rely=0.4, relwidth=0.3)
        self.button_writing.place(relx=0.35, rely=0.48, relwidth=0.3)
        self.button_stats.place(relx=0.35, rely=0.56, relwidth=0.3)

       # if checkback == 0:
      #  self.bbutton = tk.Button(text="back", command=self.backbutton())
    #    self.bbutton.place(relx=0.9, rely=0.9, relwidth=0.8)

###############################################################################
    #########################      2        ########################
###############################################################################
    def choosgamepage(self):

        config.page = 2
        global  checkback

        if checkback == 1:
            self.bbutton.destroy()
            checkback = 0

        self.label_name.set("{0} WYBIERZ JĘZYK DO NAUKI: ".format(config.nick))

        def choospolish():
            config.langchoos = 'polish'
            self.button_polish.destroy()
            self.button_english.destroy()
            if config.typechoos == 1:
                self.type1()
            elif config.typechoos == 2:
                self.type2()

        def choosenglish():
            config.langchoos = 'english'
            self.button_polish.destroy()
            self.button_english.destroy()
            if config.typechoos == 1:
                self.type1()
            elif config.typechoos == 2:
                self.type2()

        self.button_polish = tk.Button(self.root, text="POLSKI", command=choospolish, width=15)
        self.button_english = tk.Button(self.root, text="ENGLISH", command=choosenglish, width=15)

        self.button_english.place(relx=0.35, rely=0.4, relwidth=0.3)
        self.button_polish.place(relx=0.35, rely=0.48, relwidth=0.3)

###############################################################################
    #########################      4        ########################
###############################################################################
    def type1(self):

        if config.langchoos == 'polish':
            lang = 'POLSKIM'
        elif config.langchoos == 'english':
            lang = 'ANGIELSKI'


        config.page = 4

        self.label_name.set("NAUKA SŁÓWEK W JĘZYKU {}".format(lang))

        def show():
            self.label_name3.set(tryby.check1())

        def next():
            self.label_name2.set(tryby.game())
            self.label_name3.set("")

        self.label_name2 = tk.StringVar()
        self.label_name3 = tk.StringVar()
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, font=50).place(relx=0.35, rely=0.4, relwidth=0.3)
        self.label_name2.set(tryby.game())
        self.label3 = tk.Label(self.root, textvariable=self.label_name3, font=50).place(relx=0.35, rely=0.5, relwidth=0.3)



        self.button_next = tk.Button(self.root, text="POKAŻ", command=show, width=15)
        self.button_show = tk.Button(self.root, text="NASTĘPNE", command=next, width=15)
        self.button_next.place(relx=0.33, rely=0.6, relwidth=0.15)
        self.button_show.place(relx=0.52, rely=0.6, relwidth=0.15)





###############################################################################
    #########################      5        ########################
###############################################################################
    def type2(self):

        if config.langchoos == 'polish':
            lang = 'POLSKIM'
        elif config.langchoos == 'english':
            lang = 'ANGIELSKIM'

        config.page = 5

        self.label_name.set("NAUKA SŁÓWEK W JĘZYKU {} \n\n PRZETŁUMACZ SŁOWO, A NASTĘPNIE ZATWIERDZ!".format(lang))

        self.label_name2 = tk.StringVar()
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, font=50).place(relx=0.35, rely=0.5, relwidth=0.3)

        self.label_name2.set(tryby.game())

        self.wor = tk.Entry(self.root)
        self.wor.place(relx=0.35, rely=0.6, relwidth=0.3)

        def check(foo):
            if foo == tryby.check2(foo):
                msb.showinfo("info", 'Gratulacje!\nDobrze')
            else:
                msb.showinfo("info", 'Poprawne słowo to: {0}'.format(tryby.check1()))
            self.label_name2.set(tryby.game())
            self.wor.delete(0, tk.END)

        self.send = tk.Button(self.root, text="ZATWIERDZ", command=lambda: check(self.wor.get()) , width=15)
        self.send.place(relx=0.7, rely=0.6, relwidth=0.15)



    # def backbutton(self):
    #     global checkback
    #     checkback = 1
    #     if config.page == 3:
    #         self.button_learning.destroy()
    #         self.button_writing.destroy()
    #         self.choosgamepage()
    #     elif config.page == 4:
    #         self.choostyppage()
    #     elif config.page == 5:
    #         self.choostyppage()




root = tk.Tk()
app = App(root)
root.geometry("600x600")
root.title("Aplikacja do fiszek")
root.mainloop()



# class MainButton(tk.Frame):
#     def __init__(self, okno):
#         super().__init__()
#         self["height"] = 150
#         self["width"] = 150
#         self["relief"] = RAISED
#         self["bd"] = 8
#        self["bg"] = "red"

# def text(self):
#     self.frame2 = tk.Frame(self.root)
#     self.frame2.pack(side="left", fill=tk.BOTH, expand=1)
#     self.txt = tk.Text(self.frame2)
#     self.txt['bg'] = 'gold'
#     self.txt.pack(fill=tk.BOTH, expand=1)

# self.lb = tk.Listbox(self.frame1)
# self.lb['bg'] = "black"
# self.lb['fg'] = "lime"
# self.lb.pack(side="left", fill=tk.BOTH, expand=1)
# for file in glob.glob("*"):
#     self.lb.insert(tk.END, file)

# def hide(self):
#     if self.hidden == 0:
#         self.frame1.destroy()
#         self.hidden = 1
#         print("Hidden", self.hidden)
#     else:
#         self.frame2.destroy()
#         self.main()
#         self.text()
#         self.hidden = 0
#         print("Hidden", self.hidden)

