#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Callable, Mapping, Optional, List
import os
import datetime
import obsluga_bazy

from gui import *

max_points: int = 14            #maksymalna liczba punktów do uzyskania w jednej turze gry

word: List[str]

def game() -> str:     # mode: 0 - nic, 1 - ang_pol, 2 - pol_ang, 3 - nauka

    word: List[str] = obsluga_bazy.all_base.get_random_pair()
                                      # typechoos = 1 nauka, 2 wpisywanie
    if langchoos == "polish":
        return word[0]
    elif langchoos == "english":
        return word[1]

def check1() -> str:
    if langchoos == "polish":
        return word[1]
    elif langchoos == "english":
        return word[0]

def check2(received_word: str) -> str:
    if langchoos == "polish":
        if received_word == word[1]:
            f = open("users_words\\" + nick + ".txt", "a", encoding="utf-8")
            f.write(str(word) + " \n")
            f.close()
        return word[1]
    elif langchoos == "english":
        if received_word == word[0]:
            f = open("users_words\\" + nick + ".txt", "a", encoding="utf-8")
            f.write(str(word) + " \n")
            f.close()
        return word[0]

"""

    points: int = 0

    for i in range(0, max_points):                  #Funkcja losuje słowo i sprawdza czy nie powtarza się z niedawno użytym
        word: List[str] =  obsluga_bazy.all_base.get_random_pair()
        f = open("users_words\\" + nick + ".txt" , "r", encoding="utf-8")
        while str(word) in f.readlines():
            print("powtórzone słowo" + str(word))
            word = obsluga_bazy.all_base.get_random_pair()
        #f.close()


        if mode == 1:
            if Foo(word[0]) == word[1]:        # Foo - nazwa tymczasowa
                points += 1
                f = open("users_words\\" + nick + ".txt", "a", encoding="utf-8")
                f.write(str(word) + " \n")
                f.close()
        elif mode == 2:
            if Foo(word[1]) == word[0]:        # Foo - nazwa tymczasowa
                points += 1
                f = open("users_words\\" + nick + ".txt", "a", encoding="utf-8")
                f.write(str(word) + " \n")
                f.close()
        elif mode == 3:
            Foo2(word[0] + " - " + word[1])     # Foo2 - nazwa tymczasowa

    f = open("statistics\\" + nick + ".txt", "a")
    f.write(str(datetime.datetime.now()) + " - " + str(points) + " \n")           #zapisanie liczby uzyskanych punktów do pliku
    f.close()
#---------------------------------------------------------------------------------------------------------------------------------




def Foo(word: str) -> str:                      #Funkcja tymczasowa do testowania kodu
    print(word)
    return input("")
#--------------------------------------------------------------------------------------------------------------------------------





def words_statistics() -> None:                 #Funkcja sterująca statystykami
    print(os.getcwd())
    folders = os.listdir("users_words")
    print(folders)
    for i in folders:
        print(i)
        f = open("users_words\\" + i, 'r', encoding="utf-8")
        lines: List[str] = f.readlines()
        f.close()

"""
