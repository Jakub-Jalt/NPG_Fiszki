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

        self.label_name.set("WITAJ W APLIKACJI DO NAUKI \n POPRZEZ FISZKI !!! \n\n\n PODAJ SWOJE IMIĘ: ")

        self.name = tk.Entry(self.root)
        self.name.place(relx=0.25, rely=0.4, relwidth=0.3)

        self.button_ok = tk.Button(self.root, width=10, text="OK", command=lambda: hello(), relief="raised", default="active", )
        self.button_ok.place(relx=0.6, rely=0.4, relwidth=0.15)

        def hello():
            name = self.name.get()  # przypisanie imienia do zmiennej globalnej
            config.nick = name.upper()
            if config.nick == "":
                msb.showinfo("info", 'PODAJ SWOJE IMIĘ !!!')
            else:
                msb.showinfo("info", 'WITAJ, {0}\nTERAZ CZEKA CIĘ NAUKA :)'.format(config.nick))
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

        self.button_learning = tk.Button(self.root, text="NAUKA", command=type1, width=15, bg="orange")
        self.button_writing = tk.Button(self.root, text="WYPISYWANIE", command=type2, width=15, bg="teal")
        self.button_stats = tk.Button(self.root, text="STATYSTYKI", command=stat, width=15, bg="fuchsia")
        self.button_addword = tk.Button(self.root, text="DODAJ SŁOWA", command=addw, width=15, bg="olive")
        self.button_learning.place(relx=0.35, rely=0.3, relwidth=0.3)
        self.button_writing.place(relx=0.35, rely=0.38, relwidth=0.3)
        self.button_stats.place(relx=0.35, rely=0.46, relwidth=0.3)
        self.button_addword.place(relx=0.35, rely=0.54, relwidth=0.3)


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

        self.back_button = tk.Button(self.root, command=back, text="<--")
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

        self.button_polish = tk.Button(self.root, text="POLSKI", command=choospolish, width=15, bg="white")
        self.button_english = tk.Button(self.root, text="ENGLISH", command=choosenglish, width=15, bg="red")

        self.button_english.place(relx=0.35, rely=0.38, relwidth=0.3)
        self.button_polish.place(relx=0.35, rely=0.3, relwidth=0.3)

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
            self.label_name2.set("")
            self.label_name3.set("")
            self.back_button.destroy()
            self.choosgamepage()

        self.back_button = tk.Button(self.root, command=back, text="<--")
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



        self.button_next = tk.Button(self.root, text="POKAŻ", command=show, width=15, bg="aqua")
        self.button_show = tk.Button(self.root, text="NASTĘPNE", command=next, width=15, bg="orange")
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
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, font="50").place(relx=0.35, rely=0.35, relwidth=0.3)

        self.label_name2.set(tryby.game())

        def back():
            self.label_name2.set("")
            self.send.destroy()
            self.wor.destroy()
            self.button_save.destroy()
            self.back_button.destroy()
            self.choosgamepage()


        self.wor = tk.Entry(self.root)
        self.wor.place(relx=0.35, rely=0.45, relwidth=0.3)

        def check(foo):
            if foo == tryby.check2(foo):
                msb.showinfo("info", 'GRATULACJE !!!\nDOBRZE')
            else:
                msb.showinfo("info", 'Poprawne słowo to: {0}'.format(tryby.check1()))
            self.label_name2.set(tryby.game())
            self.wor.delete(0, tk.END)

        self.send = tk.Button(self.root, text="ZATWIERDZ", command=lambda: check(self.wor.get()) , width=15, bg="orange")
        self.send.place(relx=0.7, rely=0.45, relwidth=0.15)

        self.button_save = tk.Button(self.root, text="ZAPISZ SESJE !!!", width=15, bg="olive") # komendaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        self.button_save.place(relx=0.35, rely=0.6, relwidth=0.3)

        self.back_button = tk.Button(self.root, command=back, text="<--")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

###############################################################################
    #########################      6        ########################
###############################################################################
    def staty(self):

        config.page = 6

        def back():
            self.label_name2.set("")
            self.back_button.destroy()
            self.choostyppage()

        self.back_button = tk.Button(self.root, command=back, text="BACK")
        self.back_button.place(relx=0.89, rely=0.95, relwidth=0.1)

        self.label_name.set("STATYSTYKI NAUKI")

        self.label_name2 = tk.StringVar()
        self.label2 = tk.Label(self.root, textvariable=self.label_name2, justify="left", font = 40).place(relx=0.1, rely=0.3, relwidth=0.8)
        self.label_name2.set(mode_stat.show_stats_full())

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
            self.label_name2.set("")
            self.choostyppage()

        self.back_button = tk.Button(self.root, command=back, text="<--")
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

        self.button_send = tk.Button(self.root, text="ZATWIERDZ", command=send, width=15, bg="orange")
        self.button_send.place(relx=0.55, rely=0.52, relwidth=0.15)

root = tk.Tk()
app = App(root)
root.geometry("600x600")
root.title("Aplikacja do fiszek")
root.mainloop()


