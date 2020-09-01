import tkinter as tk
import time

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def base(self):
        global p1
        global p2
        global p3
        p1 = PageMain(self)
        p2 = Page2(self)
        p3 = Page3(self)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class PageMain(Page):
    def __init__(self, *args, **kwargs):
        global imie                                # zmienna imie
        Page.__init__(self, *args, **kwargs)
        etykieta = tk.StringVar()
        label = tk.Label(self, textvariable=etykieta)
        etykieta.set("Witaj w aplikacji do nauki \n poprzez Fiszki !!! \n\n podaj swoje imie: ")
        name = tk.Entry(self, width=30)
        label.grid(row=2, column=2)
        name.grid(row=3, column=2)
        def hello():
            etykieta.set("Witaj, {0}\n teraz czeka cię nauka :)".format(name.get()))
            imie = name
            name.delete(0, 'end')
            time.sleep(1)


        ok = tk.Button(text="OK", command=hello)
        ok.pack()


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)


# class MainButton(tk.Frame):
#     def __init__(self, okno):
#         super().__init__()
#         self["height"] = 150
#         self["width"] = 150
#         self["relief"] = RAISED
#         self["bd"] = 8
#         self["bg"] = "red"




def topmenu(root):
    menu = tk.Menu(root)
    menutop = tk.Menu(menu, tearoff=0)
    menutop.add_command(label="P1", command=p1.lift)
    menutop.add_command(label="P2", command=p2.lift)
    menutop.add_command(label="P3", command=p3.lift)
    menu.add_cascade(label="Opcje", menu=menutop)
    root.config(menu=menu)


def main():
    root = tk.Tk()
    main = MainView(root)
    main.base()
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.title("Aplikacja do fiszek")
    topmenu(root)
    root.mainloop()
