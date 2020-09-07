import tkinter as tk
from tkinter import messagebox as msb
import time
import glob
import tryby


langchoos = 'null'
typechoos = 1
nick = 'user'
page = 0


class App:

    def __init__(self, root):
        self.root = root
        self.main()

###############################################################################
    #########################      1        ########################
###############################################################################
    def main(self):
        global page
        page = 1

        self.frame1 = tk.Frame(self.root)

        self.label_name = tk.StringVar()
        self.label = tk.Label(self.frame1, textvariable=self.label_name,relief = "raised", font=42 ).pack(side="top", pady=20)
        self.name = tk.Entry(self.frame1)
        self.name.pack(side="top")
        self.label_name.set("Witaj w aplikacji do nauki \n poprzez Fiszki !!! \n\n podaj swoje imie: ")

        self.button_ok = tk.Button(self.frame1, text="OK", command=lambda: hello(self.name.get()), width=5)
        self.button_ok.pack(side="top",pady=5)
        self.frame1.pack(fill="both", expand=True)

        def hello(name):
            global nick
            print(str)
            msb.showinfo("info", 'Witaj, {0}\n teraz czeka cię nauka :)'.format(name))
            nick = name  # przypisanie imienia do zmiennej globalnej
            self.frame1.destroy()
            self.choosgamepage()
###############################################################################
    #########################      2        ########################
###############################################################################
    def choosgamepage(self):
        global page
        global nick

        page = 2

        self.frame2 = tk.Frame(self.root)

        self.label_name = tk.StringVar()
        self.label = tk.Label(self.frame2, textvariable=self.label_name, font=42).pack(side="top", pady=20)
        self.label_name.set("{0} wybierz jezyk do nauki: ".format(nick))

        def choospolish():
            global langchoos
            langchoos = 'polish'
            self.frame2.destroy()
            self.choostyppage()

        def choosenglish():
            global langchoos
            langchoos = 'english'
            self.frame2.destroy()
            self.choostyppage()

        self.button_polish = tk.Button(self.frame2, text="POLSKI", command=choospolish, width=15)
        self.button_english = tk.Button(self.frame2, text="ENGLISH", command=choosenglish, width=15)
        self.button_english.pack(side="top", pady=5)
        self.button_polish.pack(side="top", pady=5)

        self.frame2.pack(fill="both", expand=True)
###############################################################################
    #########################      3        ########################
###############################################################################
    def choostyppage(self):

        global page

        page = 3

        self.frame3 = tk.Frame(self.root)

        self.label_name = tk.StringVar()
        self.label = tk.Label(self.frame3, textvariable=self.label_name, font=42).pack(side="top", pady=20)
        self.label_name.set("Wybierz tryb nauki: ")

        def type1():
            global typechoos
            langchoos = 1
            self.frame3.destroy()
            self.type1()
        def type2():
            global typechoos
            langchoos = 2
            self.frame3.destroy()
            self.type2()

        self.button_learning = tk.Button(self.frame3, text="NAUKA", command=type1, width=15)
        self.button_writing = tk.Button(self.frame3, text="WYPISYWANIE", command=type2, width=15)
        self.button_learning.pack(side="top", pady=5)
        self.button_writing.pack(side="top", pady=5)

        self.frame3.pack(fill="both", expand=True)

###############################################################################
    #########################      4        ########################
###############################################################################
    def type1(self):
        global page
        global langchoos
        lang = 'random'
        if langchoos == 'polish':
            lang = 'polskim'
        if langchoos == 'english':
                lang = 'angielskim'


        page = 4

        self.frame4 = tk.Frame(self.root)

        self.label_name = tk.StringVar()
        self.label = tk.Label(self.frame4, textvariable=self.label_name, font=42).pack(side="top", pady=20, fill=tk.Y)
        self.label_name.set("Nauka słówek w języku {}".format(lang))

        def show():
            self.label_name3.set("Slowko odkryte")

        def newu():
            self.label_name2.set("Nowe slowo")
            self.label_name3.set("")

        self.label_name2 = tk.StringVar()
        self.label_name3 = tk.StringVar()
        self.label2 = tk.Label(self.frame4, textvariable=self.label_name2, font=50).pack(side="top", pady=30,fill=tk.Y)
        self.label_name2.set("Slowko po ang lub pol")
        self.label3 = tk.Label(self.frame4, textvariable=self.label_name3, font=50).pack(side="top", pady=30, fill=tk.Y)



        self.button_learning = tk.Button(self.frame4, text="Odkryj", command=show, width=15)
        self.button_writing = tk.Button(self.frame4, text="WYPISYWANIE", command=newu, width=15)
        self.button_learning.pack(side="top", pady=5, fill=tk.Y)
        self.button_writing.pack(side="top", pady=5, fill=tk.Y)

        self.frame4.pack(expand=True, fill=tk.BOTH)

###############################################################################
    #########################      5        ########################
###############################################################################
    def type2(self):
        global page
        global langchoos
        lang = 'random'
        if langchoos == 'polish':
            lang = 'polskim'
        if langchoos == 'english':
                lang = 'angielskim'


        page = 5

        self.frame5 = tk.Frame(self.root)

        self.label_name = tk.StringVar()
        self.label = tk.Label(self.frame5, textvariable=self.label_name, font=42).pack(side="top", pady=20, fill=tk.Y)
        self.label_name.set("Nauka słówek w języku {}".format(lang))

        def communication(i):
            show(i)
            return(self.word)

        def show(i):
            self.label_name3.set(i)

        def newu():
            self.label_name2.set(tryby.game(2))


        self.label_name2 = tk.StringVar()
        self.label_name3 = tk.StringVar()
        self.label2 = tk.Label(self.frame5, textvariable=self.label_name2, font=50).pack(side="top", pady=30,fill=tk.Y)
        newu()
        self.label3 = tk.Label(self.frame5, textvariable=self.label_name3, font=50).pack(side="top", pady=30, fill=tk.Y)

        self.word = tk.Entry(self.frame5)
        self.word.pack(side="top")


        self.send = tk.Button(self.frame5, text="Zatwierdz", command=send, width=15)
        self.send.pack(side="top", pady=5, fill=tk.Y)

        self.frame5.pack(expand=True, fill=tk.BOTH)




root = tk.Tk()
app = App(root)
root.geometry("400x400")
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

