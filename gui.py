import tkinter as tk
from tkinter import messagebox as msb
import tryby
import config
import mode_stat
import mode_edit
import mode_new

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
                config.nick = name  # przypisanie imienia do zmiennej globalnej
                msb.showinfo("info", 'Witaj, {0}\n teraz czeka cię nauka :)'.format(config.nick))
                self.button_ok.destroy()
                self.name.destroy()
                mode_new.check_user()
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
            self.button_addword.destroy()
            self.choosgamepage()

        def type2():  # wpisywanie
            config.typechoos = 2
            self.button_writing.destroy()
            self.button_learning.destroy()
            self.button_stats.destroy()
            self.button_addword.destroy()
            self.choosgamepage()

        def stat():  # statystyki
            config.typechoos = 4
            self.button_writing.destroy()
            self.button_learning.destroy()
            self.button_stats.destroy()
            self.button_addword.destroy()
            self.staty()

        def addw():  # dodawanie slow
            config.typechoos = 5
            self.button_writing.destroy()
            self.button_learning.destroy()
            self.button_stats.destroy()
            self.button_addword.destroy()
            self.add()

        self.button_learning = tk.Button(self.root, text="NAUKA", command=type1, width=15)
        self.button_writing = tk.Button(self.root, text="WYPISYWANIE", command=type2, width=15)
        self.button_stats = tk.Button(self.root, text="STATYSTYKI", command=stat, width=15)
        self.button_addword = tk.Button(self.root, text="DODAJ SŁOWA", command=addw, width=15)
        self.button_learning.place(relx=0.35, rely=0.4, relwidth=0.3)
        self.button_writing.place(relx=0.35, rely=0.48, relwidth=0.3)
        self.button_stats.place(relx=0.35, rely=0.56, relwidth=0.3)
        self.button_addword.place(relx=0.35, rely=0.64, relwidth=0.3)


###############################################################################
    #########################      3        ########################
###############################################################################
    def choosgamepage(self):

        config.page = 3

        def back():
            self.button_english.destroy()
            self.button_polish.destroy()
            self.back_button.destroy()
            self.choostyppage()

        self.back_button = tk.Button(self.root, command=back, text="BACK")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

        self.label_name.set("{0} WYBIERZ JĘZYK DO NAUKI: ".format(config.nick))

        def choospolish():
            config.langchoos = 'polish'
            self.button_polish.destroy()
            self.button_english.destroy()
            self.back_button.destroy()
            if config.typechoos == 1:
                self.type1()
            elif config.typechoos == 2:
                self.type2()

        def choosenglish():
            config.langchoos = 'english'
            self.button_polish.destroy()
            self.button_english.destroy()
            self.back_button.destroy()
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
            lang: str = "POLSKIM"
        elif config.langchoos == 'english':
            lang: str = "ANGIELSKI"


        config.page = 4

        def back():
            self.button_show.destroy()
            self.button_next.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.back_button.destroy()
            self.choosgamepage()

        self.back_button = tk.Button(self.root, command=back, text="BACK")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

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
            lang: str = "POLSKIM"
        elif config.langchoos == 'english':
            lang: str = "ANGIELSKIM"

        config.page = 5




        self.label_name.set("NAUKA SŁÓWEK W JĘZYKU {} \n\n PRZETŁUMACZ SŁOWO, A NASTĘPNIE ZATWIERDZ!".format(lang))

        self.label_name2 = tk.StringVar()
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, font=50).place(relx=0.35, rely=0.5, relwidth=0.3)

        self.label_name2.set(tryby.game())

        def back():
            self.label_name2.destroy()
            self.send.destroy()
            self.wor.destroy()
            self.choosgamepage()
            self.back_button.destroy()

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

        self.back_button = tk.Button(self.root, command=back, text="BACK")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

###############################################################################
    #########################      6        ########################
###############################################################################
    def staty(self):

        config.page = 6

        def back():
            self.label2.destroy()
            self.back_button.destroy()
            self.choostyppage()

        self.back_button = tk.Button(self.root, command=back, text="BACK")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

        self.label_name.set("STATYSTYKI NAUKI")

        stat = mode_stat.show_stats()

        self.label_name2 = tk.StringVar()
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, font=50).place(relx=0.1, rely=0.3, relwidth=0.8)
        self.label_name2.set("#1 - data dnia rozgrywek: {0} \n#2 - liczba odbytych rozgrywek: {1} \n#3 - liczba łącznie wyświetlonych słów: {2} \n#4 - liczba łącznie odgadniętych słów w wersji polskiej: {3} \n#5 - liczba łącznie odgadniętych słów w wersji angielskiej: {4}  ".format(stat[0],stat[1],stat[2],stat[3],stat[4]))

###############################################################################
    #########################      7        ########################
###############################################################################
    def add(self):

        config.page = 7

        def back():
            self.word_polish.destroy()
            self.word_english.destroy()
            self.button_send.destroy()
            self.back_button.destroy()
            self.choostyppage()

        self.back_button = tk.Button(self.root, command=back, text="BACK")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

        self.label_name.set("DODAWANIE SŁÓWEK")

        def send():
            wordpol:str=self.word_polish.get()
            wordeng:str=self.word_english.get()
            pair = [wordeng, wordpol]
            mode_edit.add_words(pair)
            self.word_english.delete(0, tk.END)
            self.word_polish.delete(0, tk.END)


        self.label_name2 = tk.StringVar()
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, font=50).place(relx=0.2, rely=0.4)
        self.label_name2.set("SŁÓWKO PO ANGIELSKU: \n\n SŁÓWKO PO POLSKU: ")

        self.word_english = tk.Entry(self.root)
        self.word_english.place(relx=0.55, rely=0.4, relwidth=0.3)
        self.word_polish = tk.Entry(self.root)
        self.word_polish.place(relx=0.55, rely=0.465, relwidth=0.3)

        self.button_send = tk.Button(self.root, text="ZATWIERDZ", command=send, width=15)
        self.button_send.place(relx=0.55, rely=0.52, relwidth=0.15)






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

